from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from django.utils.decorators import method_decorator
from scouts.decorators import group_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test

from login.groups import Groups

from leaders.forms import BadgeForm
from leaders.models import ScoutData
from django.contrib.auth.models import User
from accounts.models import UserProfile, GroupRecord

from leaders.badge_report import Badge_Reporter

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

# Create your views here
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

		args = {}
		return render(request, self.template_name, args)

@method_decorator(staff_member_required, name='get')
class Badge_Report(TemplateView):
	def get(self, request, month):

		args = {}
		return Badge_Reporter.Badge_Report(self, request, month)


@method_decorator(staff_member_required, name='get')
class SubmitedView(TemplateView):
	template_name = 'leaders/form_redirect.html'
	
	def get(self, request):


		args = {}
		return render(request, self.template_name, args)

class testView(TemplateView):
	template_name = 'leaders/test.html'
	def get(self, request):
		results = Groups.Groups_finder

		args = {'list': results}
		return render(request, self.template_name, args)


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