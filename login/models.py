#in case having the troop details within the userprofile does not work

from django.db import models
from django.contrib.auth.models import User

from login.groups import Groups

# Create your models here.

class ScoutGroupManager(models.Manager):
	def get_queryset(self):
		return super(Scout_Group, self).get_queryset()

class ScoutGroup(models.Model):

	Group_Choice = Groups.Scout_Groups()
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	Troop = models.SlugField(max_length=27, choices=Group_Choice, default='None', blank=False)
