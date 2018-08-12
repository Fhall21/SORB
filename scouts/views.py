from django.contrib.auth.models import User
from django.views.generic import TemplateView


from django.urls import reverse

class Login_Error_redirect(TemplateView):
	def get(self, request):
		return redirect('login:login')

