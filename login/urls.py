from django.urls import path, re_path
from login import views
from django.contrib.auth.views import login
from login.views import Login, Register

from django.contrib.auth.views import (
	password_reset, password_reset_done, password_reset_confirm, 
	password_reset_complete
	)


app_name="login"

urlpatterns = [
	path('', Login.as_view(), name='login'),
	#setting up accounts, to look over later
	path('register', Register.as_view(), name='register'),
	path('reset-password/', password_reset, 
		{'template_name': 'login/reset_password.html', 
		'post_reset_redirect': 'login:password_reset_done', 
		'email_template_name': 'login/reset_password_email.html',
		}, name='reset_password'),

	path('reset-password/done/', password_reset_done, 
		{'template_name': 'login/reset_password_done.html'}, name='password_reset_done'),
	
	re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
		password_reset_confirm, {'template_name': 'login/reset_password_confirm.html', 
		'post_reset_redirect': 'login:password_reset_complete'},  
		name='password_reset_confirm'),

	path('reset-password/complete/', password_reset_complete, 
		{'template_name': 'login/reset_password_complete.html'},
	 name="password_reset_complete"),

	] 