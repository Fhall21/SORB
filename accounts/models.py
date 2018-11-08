from django.db import models
from django.contrib.auth.models import AbstractUser

from crequest.middleware import CrequestMiddleware


from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from datetime import date
import inspect, os
from django.dispatch import receiver


#from login.groups import Groups

# Create your models here.
def list_maker(abbr, name):
	list_group = (str(abbr), str(name))
	return list_group


class GroupRecord(models.Model):
	plan_choice = (
		('Basic', 'Basic'),
		('Premium', 'Premium')
		)
	group = models.CharField(max_length=100)
	abbreviation = models.CharField(max_length=80)
	subscription = models.CharField(choices=plan_choice, max_length=8, default='Basic', blank=False)




	def __str__(self):
		return '%s'% (self.group)

def Scout_Groups():
		
		scout_group_list = (
		(None, 'Click here to select the group'),
		('BC', 'Brisbane Central Scout'),
		('Admin', 'N/A'),

		)
		return scout_group_list

'''
class UserProfileAdminManager(models.AdminManager):
	def get_query_set(self, request):
		return super(UserProfileAdminManager, self).get_query_set().filter(troop=request.user.userprofile.troop)
'''
class UserProfile(models.Model):

	list_format_group = [(None, 'Click here to select the group')]

#	list_format_group = []
	data_set = GroupRecord.objects.all()
	for i in data_set:
		group_name = i.group
		group_abbr = i.abbreviation
		list_format_group.append(list_maker(group_abbr, group_name))
	tuple_format_group = tuple(list_format_group)
	scout_username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	Group_Choice = tuple_format_group
	role_choice = (
		('Leader', 'Leader'),
		('Scout', 'Scout')
		)
#	troop = models.ForeignKey(GroupRecord, on_delete=models.CASCADE, null=True)
	troop = models.SlugField(max_length=27, choices=Group_Choice, default='None', blank=False)
	role = models.CharField(choices = role_choice, max_length=7, default='Scout', blank=False)
	date_of_birth = models.DateField(default=date.today, null=True)


	def __str__(self):
		return '%s'% (self.scout_username)

		
	def save(self, *args, **kwargs):
		
			Leader_group = Group.objects.get(name="Leader")
			Scout_group = Group.objects.get(name="Scouts")

			Premium_group = Group.objects.get(name="Premium")
			Basic_group = Group.objects.get(name="Basic")
			CurrentTroopData = GroupRecord.objects.filter(abbreviation=self.troop)

			user = self.scout_username
			user.groups.clear()
			if self.role == 'Leader':
				Leader_group.user_set.add(user)
			elif self.role == 'Scout':
				Scout_group.user_set.add(user)
			else:
				pass
			if (CurrentTroopData.filter(subscription="Premium").exists()):
				Premium_group.user_set.add(user)
			elif (CurrentTroopData.filter(subscription="Basic").exists()):
				Basic_group.user_set.add(user)
			else:
				pass
			super(UserProfile, self).save(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs): 
	if created:
		print ('instance is: {}'.format(instance))

		for entry in reversed(inspect.stack()):
#			print (entry[0].f_locals['request'].user)
			try:
				current_request = CrequestMiddleware.get_request()
				user = current_request.user
			#	user = entry[0].f_locals['request'].user
			except:
				user = None
			break
		if user:
			try:
				UserProfile.objects.create(scout_username=instance, 
					troop=user.userprofile.troop)
			except (AttributeError):
				UserProfile.objects.create(scout_username=instance) 
				#do not create now
				#then create in views
				pass
			
		else:
			UserProfile.objects.create(scout_username=instance)
	instance.userprofile.save()


post_save.connect(create_user_profile, sender=User)

class UserProfileManager(models.Manager):
	def get_queryset(self, request):
		query =	UserProfile.objects.filter(troop=request.user.userprofile.troop)
		if request.user.is_superuser:
			query = UserProfile.objects.all()
		return query

class UserManager(models.Manager):
	def get_queryset(self, request):
		query =	User.objects.filter(userprofile__troop=request.user.userprofile.troop)
		if request.user.is_superuser:
			query = User.objects.all()
		return query

'''
class ScoutUser(AbstractUser):
	list_format_group = [(None, 'Click here to select the group')]
	data_set = GroupRecord.objects.all()
	for i in data_set:
		group_name = i.group
		group_abbr = i.abbreviation
		list_format_group.append(list_maker(group_abbr, group_name))
	tuple_format_group = tuple(list_format_group)
	scout_username = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
	Group_Choice = tuple_format_group
	role_choice = (
		('Leader', 'Leader'),
		('Scout', 'Scout')
		)
#	troop = models.ForeignKey(GroupRecord, on_delete=models.CASCADE, null=True)
	troop = models.SlugField(max_length=27, choices=Group_Choice, default='None', blank=False)
	role = models.CharField(choices = role_choice, max_length=7, default='Leader', blank=False)
	date_of_birth = models.DateField(default=date.today, null=True)
'''