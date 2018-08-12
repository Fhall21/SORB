from django.views.generic import TemplateView
from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView

from accounts.forms import RegistrationForm

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from accounts.models import UserProfile, UserProfileManager
from login.userprofile_finder import UserProfileGetter 
# Create your views here.






		
class Login(TemplateView):
	template_name = 'login/login.html'


	def get(self, request):
		form = AuthenticationForm()
		args = {'form': form}

		

		return render(request, self.template_name, args)

	def post(self, request):
		def is_leader(user):
			return user.groups.filter(name='Leader').exists()

		def is_scout(user):
			return user.groups.filter(name='Scout').exists()

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			request.session['user_username'] = username

			if is_leader(user):
				print('leader')
				redirecting_url = 'leaders:home'
				return redirect(redirecting_url)



			elif is_scout(user):
				redirecting_url = 'accounts:home'
				slug = user.userprofile.troop
				return redirect(redirecting_url, slug=slug)
			
			elif user.is_superuser:
				redirecting_url = 'admin:index'
				return redirect(redirecting_url)
			else:
				print('error')
				slug = user.userprofile.troop
				redirecting_url = 'accounts:home'
				return redirect(redirecting_url, slug=slug)

		else:
			form = AuthenticationForm()
			error = True
			args = {'form': form, 'error': error}
			return render(request, self.template_name, args)

	        
class Register(TemplateView):
	def get(request):
		form_var = RegistrationForm()
		args = {'form': form_var}
		return render(request, 'login/reg_form.html', args)
	def post(request):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('accounts:home', slug=user.userprofile.slug)


class Change_Password(TemplateView):
	def get(request):
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'login/change_password.html', args)		

	def post(request):
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('accounts:view_profile', slug=user.userprofile.slug)
		else:
			return redirect("login:change_password", slug=user.userprofile.slug)

