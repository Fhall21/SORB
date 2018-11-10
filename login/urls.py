from django.urls import path, re_path, reverse_lazy
from login import views
from login.views import Login, Register

from django.contrib.auth.views import (
	LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, 
	PasswordResetCompleteView
	)
from django.shortcuts import redirect


app_name="login"

urlpatterns = [
	path('', Login.as_view(), name='login'),
	#setting up accounts, to look over later
	path('register', Register.as_view(), name='register'),
	path('reset-password/', PasswordResetView.as_view(
		template_name= 'login/reset_password.html', 
		success_url= 'done/', 
		email_template_name= 'login/reset_password_email.html',
		), name='reset_password'),

	path('reset-password/done/', PasswordResetDoneView.as_view( 
		template_name= 'login/reset_password_done.html'), name='password_reset_done'),
	
	re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 
		PasswordResetConfirmView.as_view(
			template_name= 'login/reset_password_confirm.html', 
			success_url= reverse_lazy('login:password_reset_complete')),
			
		name='password_reset_confirm'),

	path('reset-password/complete/', PasswordResetCompleteView.as_view( 
		template_name= 'login/reset_password_complete.html'),
	 name="password_reset_complete"),

	] 
