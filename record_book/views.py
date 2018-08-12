from django.views.generic import TemplateView
from django.shortcuts import render, redirect



from django.contrib.auth.models import User

class Pioneer(TemplateView):
	template_name = 'record_book/pioneer.html'

	def get(self, request):
		user = request.user
		args = {'user': user}
		return render(request, self.template_name, args)
	