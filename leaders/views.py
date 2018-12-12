from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.utils.decorators import method_decorator
from scouts.decorators import group_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

from login.groups import Groups
from django.core.mail import EmailMessage, send_mail

from leaders.forms import BadgeForm, EmailForm
from leaders.models import ScoutData
from django.contrib.auth.models import User
from accounts.models import UserProfile, UserProfileManager, UserManager, GroupRecord

from leaders.badge_report import Badge_Reporter
from leaders.Badge_list import BadgeList

from leaders.utils import render_to_pdf

#time stuff

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone

def group_required(group_names):
	"""Requires user membership in at least one of the groups passed in."""
	try:
		user = CrequestMiddleware.get_request().user
		if user.is_authenticated():
			test = user.groups.filter(name=group_names).exists()
	except (AttributeError):
		test = False

#checks if is a Leader
def leader_check(user):
    return user.groups.filter(name__in=['Leader'])
#checks if Patrol Leader
def PL_check(user):
    return user.groups.filter(name__in=['Patrol_Leader'])

#checks if has premium access
def Premium_access(request):
	if request.user.groups.filter(name__in=['Premium']):
		premium_access = True
	else:
		premium_access = False
	return premium_access

#gets all user based on their groups (scout or leader)
def email_groups(group, user_list):
	query_list = []
	for user in user_list:
		if user.groups.filter(name__in=[group]):
			query_list.append(user)
	return query_list


@method_decorator(user_passes_test(leader_check), name='get')
class HomeView(TemplateView):
	template_name = 'leaders/home.html'

	def get(self, request):
		args = {'PremiumAccess': Premium_access(request)}
		return render(request, self.template_name, args)


#badge stuff
@method_decorator(staff_member_required, name='get')
class RequestBadgeQuantityView(TemplateView):
	template_name = 'leaders/badge_request_quantity.html'
	
	def get(self, request):

		args = {'PremiumAccess': Premium_access(request)}
		return render(request, self.template_name, args)





# scout view -- use an ORm to display data for only certain scouts. eg (ask the name of the scout) then filter the database for that data
@method_decorator(staff_member_required, name='get')
class ScoutView(TemplateView):
	template_name = 'leaders/scout_view.html'

	def get(self, request):

		args = {}
		return render(request, self.template_name, args)

@method_decorator(staff_member_required, name='get')
class Report_Quantity(TemplateView):
	template_name = 'leaders/report_quantity.html'



	def get(self, request):

		data = BadgeList(request, 1)
		pioneer = data.pioneer()

		
		print(list(pioneer))
		for e in list(pioneer):
			print(pioneer[e])
		args = {}
		return render(request, self.template_name, args)

@method_decorator(staff_member_required, name='get')
class Badge_Report(TemplateView):
	def get(self, request, month):


		#getting troop name
		_abbreviation = request.user.userprofile.troop
		#GP refers to GroupRecord
		GP_data = GroupRecord.objects.filter(abbreviation=_abbreviation)
		GP_entry = GP_data[0]
		_troop = GP_entry.group
		#temp
		print(_troop)

		#times
		current_time = timezone.now()
		last_time = (current_time - relativedelta(months=month)).strftime("%d-%B %Y")
		current_time_strf = current_time.strftime("%d-%B %Y")



		pdf = render_to_pdf(request, 'pdf/badge_report.html', month=month, time_now=current_time_strf, time_then=last_time, troop=_troop)
		if pdf:
			
			response =  HttpResponse(pdf, content_type='application/pdf')
			filename = "Badge Report"
			content = "inline; filename='%s'" %(filename)
			download = request.GET.get("download")
			if download:
				content = "attachment; filename='%s'" %(filename)
			response['Content-Disposition'] = content
			return response
		return HttpResponse("Not Found")
		args = {}

		#return Badge_Reporter.Badge_Report(self, request, month)


@method_decorator(staff_member_required, name='get')
class SubmitedView(TemplateView):
	template_name = 'leaders/form_redirect.html'
	
	def get(self, request):


		args = {}
		return render(request, self.template_name, args)

class ContactView(TemplateView):
	template_name = 'leaders/contact.html'
	def get(self, request):


		form = EmailForm()

		args = {'form': form}
		return render(request, self.template_name, args)

	def post(self, request):
		#getting all email addreses
		#getting all users

		#getting form info
		form = EmailForm()		
		args = {'form': form}

		form_info = EmailForm(request.POST)
		if form_info.is_valid():
			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')
			_group = request.POST.get('group', '')

			#To whom are we sending, scouts, leader? Everyone??
			#get all members from troop
			results = User.objects.filter(userprofile__troop=request.user.userprofile.troop)
			
			every_user_list = []
			for user in results:
				every_user_list.append(user)

			#filtering bsaed on role
			if _group == 'Leader' or _group == 'Scouts':
				refined_user_list = email_groups(_group, every_user_list)
			else:
				refined_user_list = every_user_list
			#getting emails
			email_list = []
			for user in refined_user_list:
				email_list.append(user.email)
				email_list.append(user.userprofile.secondary_email)
			#other email stuff
			first_name = request.user.first_name
			last_name = request.user.last_name
			from_email = request.user.email

			# email the profile with contact info
			
#			template = get_template('contact_template.txt')
#			context = {
#			'first_name': first_name,
#			'last_name': last_name,
#			'email': email,
#			'subject': subject,
#			'message': message,
#			}
#			content = template.render(context)
#			email = EmailMessage(
#				"New contact form submission",
#				content,
#				subject +'',
#				['youremail@gmail.com'],
#				headers = {'Reply-To': email }
#			)
#			email.send()
			msg = '{}\nFrom\n{} {}'.format(message, first_name, last_name)
			email = EmailMessage (
				subject=subject,
				body=msg,
				from_email='email.service@sorb.com.au',
				to=email_list,
				reply_to=list(from_email),
				headers={'Content-Type': 'text/plain'})
			email.send()
			#send_mail(subject, msg, from_email, email_list, fail_silently=False,) 

			args.update({'success':True})
		return render(request, self.template_name, args)
			
			#try send_mail if it does not work




'''
		def list_maker(abbr, name):
			list_group = (str(abbr), str(name))
			return list_group

		
		list_format_group = [(None, 'Click here to select the group')]
		data_set = GroupRecord.objects.all()
		for i in data_set:
			group_name = i.group
			group_abbr = i.abbreviation
			list_format_group.append(list_maker(group_abbr, group_name))
		tuple_format_group = tuple(list_format_group)
'''


class TestView(TemplateView):
	template_name = 'leaders/test.html'
	def get(self, request):
		data = 'Replace me!'
		args = {'data': data}
		return render(request, self.template_name, args)
