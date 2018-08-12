from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfileManager, UserProfile

from datetime import date

from accounts.scout_badge_list import Scout_List
# Create your models here.

#class Filtered_Scouts(User):
#	display_list = []
#	query = User.objects.all()
#	troop = User.userprofile.troop
#	userprofile = UserProfile.objects.all()
#	selected_scouts = userprofile.filter(troop=troop)
#	for scout in selected_scouts:
#		username = str(scout.scout_username)
#		display_list.append(username)
#		
#	query = User.objects.filter(username__in=display_list)
#	return query
#		
#	class Meta:
#		proxy = True

		

class ScoutDataManager(models.Manager):
	def get_queryset(self, request):
		display_list = []
		query = ScoutData.objects.all()
		troop = request.user.userprofile.troop
		userprofile = UserProfile.objects.all()
		selected_scouts = userprofile.filter(troop=troop)
		for scout in selected_scouts:
			username = str(scout.scout_username)

			display_list.append(username)

		
		query = ScoutData.objects.filter(scout_username__username__in=display_list)
		return query

class ScoutData(models.Model):

#	filtered = Filtered_Scouts.t_filter()

	Pioneer_Choices = Scout_List.Target_Badges()
	Explorer_Choices = Scout_List.Target_Badges()
	Adventurer_Choices = Scout_List.Target_Badges()
	Proficiency_Choices = Scout_List.Proficiency_Badges()
	Other_Choice = Scout_List.Other_Badges()

	Pioneer_Badge = models.CharField(max_length=16, choices=Pioneer_Choices, default='None', blank=True)
	Explorer_Badge = models.CharField(max_length=16, choices=Explorer_Choices, default='None', blank=True)
	Adventurer_Badge = models.CharField(max_length=16, choices=Adventurer_Choices, default='None', blank=True)
	Proficiency_Badge = models.CharField(max_length=22, choices=Proficiency_Choices, default='None', blank=True)
	Other_Badge = models.CharField(max_length=27, choices=Other_Choice, default='None', blank=True)


	scout_username = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	print (User)

	def __str__(self):
		return '%s'% (self.scout_username)

'''
	from django.db import models
	from django.contrib.auth.models import User

	from accounts.st_badge_list import st_List

	class stData(models.Model):

		Pioneer_Choices = st_List.Target_Badges()
		Explorer_Choices = st_List.Target_Badges()
		Adventurer_Choices = st_List.Target_Badges()
		Proficiency_Choices = st_List.Proficiency_Badges()
		Other_Choice = st_List.Other_Badges()

		Pioneer_Badge = models.CharField(max_length=16, choices=Pioneer_Choices, default='None', blank=True)
		Explorer_Badge = models.CharField(max_length=16, choices=Explorer_Choices, default='None', blank=True)
		Adventurer_Badge = models.CharField(max_length=16, choices=Adventurer_Choices, default='None', blank=True)
		Proficiency_Badge = models.CharField(max_length=22, choices=Proficiency_Choices, default='None', blank=True)
		Other_Badge = models.CharField(max_length=27, choices=Other_Choice, default='None', blank=True)


		st_username = models.ForeignKey(User, on_delete=models.CASCADE)
		date = models.DateTimeField(auto_now=True)
		print (User)

		def __str__(self):
			return '%s'% (self.st_username)

'''
