from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


from leaders.forms import BadgeForm
from leaders.models import ScoutData
from django.contrib.auth.models import User
from accounts.models import UserProfile

from leaders.badge_report import Badge_Reporter


# Create your views here
@method_decorator(staff_member_required, name='get')
class HomeView(TemplateView):
	template_name = 'leaders/home.html'

	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		context = {'slug_arg': slug}
		return render(request, self.template_name, context)


#badge stuff
@method_decorator(staff_member_required, name='get')
class RequestBadgeQuantityView(TemplateView):
	template_name = 'leaders/badge_request_quantity.html'
	
	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		args = {'slug_arg': slug}
		return render(request, self.template_name, args)





# scout view -- use an ORm to display data for only certain scouts. eg (ask the name of the scout) then filter the database for that data
@method_decorator(staff_member_required, name='get')
class ScoutView(TemplateView):
	template_name = 'leaders/scout_view.html'

	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		args = {'slug_arg': slug}
		return render(request, self.template_name, args)

@method_decorator(staff_member_required, name='get')
class Report_Quantity(TemplateView):
	template_name = 'leaders/report_quantity.html'

	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		args = {'slug_arg': slug}
		return render(request, self.template_name, args)

@method_decorator(staff_member_required, name='get')
class Badge_Report(TemplateView):
	def get(self, request, month, **kwargs):
		slug = request.user.userprofile.troop
		args = {'slug_arg': slug}
		return Badge_Reporter.Badge_Report(month)


@method_decorator(staff_member_required, name='get')
class SubmitedView(TemplateView):
	template_name = 'leaders/form_redirect.html'
	
	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop

		args = {'slug_arg': slug}
		return render(request, self.template_name, args)