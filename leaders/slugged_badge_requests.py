from django.views.generic import TemplateView

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from leaders.forms import BadgeForm
from leaders.models import ScoutData
from django.contrib import messages


from django.shortcuts import render, redirect
from django.forms.formsets import formset_factory

#badge Requests
@method_decorator(staff_member_required, name='get')
#a view which renders a badge request form
#here the leader can add information for a badge they have awarded to a scout
#to-do: ensure that data from several forms can be passed through to the database
class SpecificBadgeRequestView_1(TemplateView):
	template_name = 'leaders/badge_request_specifics.html'

	def get(self, request, quantity, **kwargs):



		slug = request.user.userprofile.troop
		done = False
		error = False
		formset = formset_factory(BadgeForm, extra=quantity)
		data = ScoutData.objects.all()
		form_dict = []


		for i in range(1, quantity+1):
			form_dict.append(i)

		args = {'slug_arg': slug, 'formset': formset, 'data': data,
		'form_dict': form_dict, 'done':done, 'error': error,
		}
		return render(request, self.template_name, args)

#post
	def post(self, request, **kwargs):
		slug = request.user.userprofile.troop


		#url info
		path_info = request.META.get('PATH_INFO')
		print (path_info)
		quantity = int(path_info.split('/')[-1])
		formset = formset_factory(BadgeForm, extra=quantity)


		formset = formset(request.POST)
		args = {'slug_arg': slug, 'formset':formset}

		#get site to wait till all forms are saved
		#for i in range (1,quantity+1):
#			form_name = 'Form' + str(i)
		if (formset.is_valid()):
			done = True		
			args.update({'done': done})
			for form in formset:
				info = form.save(commit=False)
				info.user = form.cleaned_data['scout_username']				#try:

				Pioneer = form.cleaned_data.get('Pioneer_Badge', None) 
				Explorer = form.cleaned_data.get('Explorer_Badge', None) 
				Adventurer = form.cleaned_data.get('Adventurer_Badge', None) 
				Proficiency = form.cleaned_data.get('Proficiency_Badge', None)
				Other =  form.cleaned_data.get('Other_Badge', None)

				if Pioneer or Explorer or Adventurer or Proficiency or Other:
					info.save()
					safe = True
					args.update({'safe': safe})
					messages.success(request, "Success! {}'s form was saved!".format(info.user))

				else:
					messages.warning(request, "{}'s form submition did not go through. You forgot to select a badge!".format(info.user))
					safe = False

			else:
				error = True
				args.update({'error': error})
	#
			if safe == True:
				slug_arg = request.user.userprofile.troop
				return redirect('leaders:redirect', slug=slug_arg)



#
#



#		if form.is_valid():
#			info = form.save(commit=False)
#			info.user = form.cleaned_data['scout_username']
#			info.save()
#
			#try:
#			Pioneer = form.cleaned_data.get('Pioneer_Badge') 
#			Explorer = form.cleaned_data.get('Explorer_Badge') 
#			Adventurer = form.cleaned_data.get('Adventurer_Badge') 
#			Proficiency = form.cleaned_data.get('Proficiency_Badge')
#			Other =  form.cleaned_data.get('Other_Badge')

#			if len(Pioneer) == len(Explorer) and len(Explorer) == len(Adventurer) and len(Adventurer) == len(Proficiency) and len(Other) == len(Proficiency):
#				error = True
#				args.update({'error': error})
#			else:
#				safe =True
#				args.update({'safe':safe})
#
			#args.update({'dataX':dataX})

			#checking system
#			counter = 0
#			for field in dataX:
#				if field == None:
#					counter += 1
#					print (counter)
#
#			if counter == 4:
#				error = True
#				args.update({'error': error})
			#	pass


#			form = BadgeForm()

#			done = True		
#			args.update({'done': done})

		return render(request, self.template_name, args)
