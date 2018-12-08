from django.contrib.auth.models import User
from leaders.models import ScoutData, ScoutDataManager

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from django.utils import timezone

class BadgeList():
	def __init__(self, request, month):	
		badge_list = []
		pioneer_dict = {}
		explorer_dict = {}
		adventurer_dict = {}
		other_dict = {}

		current_time = timezone.now()

		all_badges = ScoutDataManager.get_queryset(self, request)

		for badge in all_badges:
			compare_time = badge.date + relativedelta(months=month)
			if compare_time > current_time:
				badge_list.append(badge)

		for badge in badge_list:
			scout = User.objects.get(username=badge.scout_username)
			name = "{} {}".format(scout.first_name, scout.last_name)
			if not (badge.Pioneer_Badge == ''):
				#if the badge is not in the dictionary create a value for it
				if badge.Pioneer_Badge not in pioneer_dict:
					pioneer_dict[badge.Pioneer_Badge] = []
				#add the scout's value in the key of that badge 
				pioneer_dict[badge.Pioneer_Badge].append(name)
				

			elif not (badge.Explorer_Badge == ''):
				#if the badge is not in the dictionary create a value for it
				if badge.Explorer_Badge not in explorer_dict:
					explorer_dict[badge.Explorer_Badge] = []
				#add the scout's value in the key of that badge 
				explorer_dict[badge.Explorer_Badge].append(name)
			elif not (badge.Adventurer_Badge == ''):
				#if the badge is not in the dictionary create a value for it
				if badge.Adventurer_Badge not in adventurer_dict:
					adventurer_dict[badge.Adventurer_Badge] = []
				#add the scout's value in the key of that badge 
				adventurer_dict[badge.Adventurer_Badge].append(name)
			else:
				#if the badge is not in the dictionary create a value for it
				if badge.Other_Badge not in other_dict:
					other_dict[badge.Other_Badge] = []
				#add the scout's value in the key of that badge 
				other_dict[badge.Other_Badge].append(name) 


		self.pioneer_dict = pioneer_dict
		self.explorer_dict = explorer_dict
		self.adventurer_dict = adventurer_dict
		self.other_dict = other_dict


	def pioneer(self):
		return self.pioneer_dict
	def explorer(self):
		return self.explorer_dict
	def adventurer(self):
		return self.adventurer_dict
	def other(self):
		return self.other_dict

