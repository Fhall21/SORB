from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from leaders.models import ScoutData, ScoutDataManager
from accounts.scout_badge_list import Scout_List



from django.contrib.auth.models import User

#gets the badges
class DataListRequest():
		# gets all the proficiency badges the scout has
		def Proficiency(request):
			proficiency_badge_list = []
			user = request.user
			current_badges = ScoutData.objects.all().filter(scout_username=user)
			proficiency_progress = current_badges.exclude(Proficiency_Badge='')

			for badge in proficiency_progress:
				proficiency_badge_list.append(badge.Proficiency_Badge)
			return proficiency_badge_list

		# scout's pioneer badges
		def Pioneer(request):
			#lists
			badge_progress_list = []

			#getting the data from the database
			user = request.user
			current_badges = ScoutData.objects.all().filter(scout_username=user)
			progress = current_badges.exclude(Pioneer_Badge='')

			for badge in progress:
				badge_progress_list.append(badge.Pioneer_Badge)
			return badge_progress_list


		# scout's explorer badges
		def Explorer(request):
			#lists
			badge_progress_list = []

			# data requests
			user = request.user
			current_badges = ScoutData.objects.all().filter(scout_username=user)
			progress = current_badges.exclude(Explorer_Badge='')

			for badge in progress:
				badge_progress_list.append(badge.Explorer_Badge)
			return badge_progress_list

		# scout's adventurer badges
		def Adventurer(request):
			#lists
			badge_progress_list = []

			user = request.user
			current_badges = ScoutData.objects.all().filter(scout_username=user)
			progress = current_badges.exclude(Adventurer_Badge='')

			for badge in progress:
				badge_progress_list.append(badge.Adventurer_Badge)
			return badge_progress_list

class Percentager():
	def Pioneer(request):
		counter = 0 #counts up values given from badges
		current_set = set(DataListRequest.Pioneer(request))
		proficiency_badge_set = set(DataListRequest.Proficiency(request))

		compulsory_badges_set = set(Scout_List.Compulsory_Badges_List())
		target_badges_set = set(Scout_List.Elective_Target_Badges_List())
		proficiency_badge_set_check = set(Scout_List.Proficiency_Badges_List())

		list_compulsory_badges = list(current_set.intersection(compulsory_badges_set))
		list_target_badges = list(current_set.intersection(target_badges_set))
		list_proficiency_badge = list(proficiency_badge_set.intersection(proficiency_badge_set_check))


		for badge in list_compulsory_badges:
			counter+= 20
		if int(len(list_target_badges))  > 0:
			counter += 20
		if len(list_proficiency_badge) == 1:
			counter += 20
		elif int(len(list_proficiency_badge)) > 1:
			counter += 20
		return counter

	def Explorer(request):
		counter = 0 #counts up values given from badges
		current_set = set(DataListRequest.Explorer(request))
		proficiency_badge_set = set(DataListRequest.Proficiency(request))

		compulsory_badges_set = set(Scout_List.Compulsory_Badges_List())
		target_badges_set = set(Scout_List.Elective_Target_Badges_List())
		proficiency_badge_set_check = set(Scout_List.Proficiency_Badges_List())

		list_compulsory_badges = list(current_set.intersection(compulsory_badges_set))
		list_target_badges = list(current_set.intersection(target_badges_set))
		list_proficiency_badge = list(proficiency_badge_set.intersection(proficiency_badge_set_check))


		for badge in list_compulsory_badges:
			counter+= 20
		if int(len(list_target_badges))  > 0:
			counter += 20
		if len(list_proficiency_badge) == 3:
			counter += 20
		elif int(len(list_proficiency_badge)) > 3:
			counter += 20
		return counter

	def Adventurer(request):
		counter = 0 #counts up values given from badges
		current_set = set(DataListRequest.Adventurer(request))
		proficiency_badge_set = set(DataListRequest.Proficiency(request))

		compulsory_badges_set = set(Scout_List.Compulsory_Badges_List())
		target_badges_set = set(Scout_List.Elective_Target_Badges_List())
		proficiency_badge_set_check = set(Scout_List.Proficiency_Badges_List())

		list_compulsory_badges = list(current_set.intersection(compulsory_badges_set))
		list_target_badges = list(current_set.intersection(target_badges_set))
		list_proficiency_badge = list(proficiency_badge_set.intersection(proficiency_badge_set_check))


		for badge in list_compulsory_badges:
			counter+= 20
		if int(len(list_target_badges))  > 0:
			counter += 20
		if len(list_proficiency_badge) == 5:
			counter += 20
		elif int(len(list_proficiency_badge)) > 5:
			counter += 20
		return counter


class Pioneer(TemplateView):
	template_name = 'badge_progress/progress.html'

	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		#variables
		pioneer = True
		button_type = "danger"
		colour = "color:#8B0000;"
		percent = Percentager.Pioneer(request)
		badge_type = "Pioneer"

		#lists
		badge_progress_list = DataListRequest.Pioneer(request)
		proficiency_badge_list = DataListRequest.Proficiency(request)


		args = {
		'slug_arg': slug,
		'pioneer': pioneer,
		'button_type': button_type,
		'colour': colour,
		'percent':percent,
		'badge': badge_type,
		'proficiency_badge_list': proficiency_badge_list, 
		'badge_progress_list':badge_progress_list}
		return render(request, self.template_name, args)
	

class Explorer(TemplateView):
	template_name = 'badge_progress/progress.html'
		
	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		#variables
		explorer = True
		button_type = "info"
		colour = "color:lightskyblue"
		percent = Percentager.Explorer(request)
		badge_type = "Explorer"

		#lists

		badge_progress_list = DataListRequest.Explorer(request)
		proficiency_badge_list = DataListRequest.Proficiency(request)


		args = {
		'slug_arg': slug,
		'explorer': explorer,
		'button_type': button_type,
		'colour': colour,
		'percent':percent,
		'badge': badge_type,
		'proficiency_badge_list': proficiency_badge_list, 
		'badge_progress_list':badge_progress_list}
		return render(request, self.template_name, args)



class Adventurer(TemplateView):
	template_name = 'badge_progress/progress.html'
		
	def get(self, request, **kwargs):
		slug = request.user.userprofile.troop
		#variables
		adventurer = True
		button_type = 'success'
		colour = "color:lightgreen"
		percent = Percentager.Adventurer(request)
		badge_type = "Adventurer"

		#lists

		badge_progress_list = DataListRequest.Adventurer(request)
		proficiency_badge_list = DataListRequest.Proficiency(request)

		args = {
		'slug_arg': slug,
		'adventurer':adventurer,
		'button_type': button_type,
		'colour': colour,
		'percent':percent,
		'badge': badge_type,
		'proficiency_badge_list': proficiency_badge_list, 
		'badge_progress_list':badge_progress_list}
		return render(request, self.template_name, args)
		return render(request, self.template_name, args)


