
from django import forms
from leaders.models import ScoutData, ScoutDataManager
from django.contrib.auth.models import User
from accounts.models import UserProfileManager, UserProfile

	#user1 = User.objects.get(username ='user1')

	#scout_username_list=[
	#	(None, 'Choose a scout'),
	#	(scout_user, 'user1'),
	#	(i, 'no progress'),
	#	]


# Create your models here.
class EmailForm(forms.Form):


#	email = forms.EmailField(required=True,
#		label='Email:',
#		error_messages={'required': 'It helps to have your email'},		
#)

	GroupChoices = (
		('Scouts', 'Scouts',),
		('Leader', 'Leaders',),
		('All', 'All',)
		)
	group = forms.ChoiceField(
		required=True,
		widget=forms.RadioSelect(attrs={'id':'group_radio'}),
		choices=GroupChoices,
		)

	subject = forms.CharField(required=True, 
		label='Subject:',
		error_messages={'required': 'Please select subject'},
		)

	message = forms.CharField(required=True, 
		label='Message:', 
		widget=forms.Textarea,
		max_length='500',
		min_length='10',
		error_messages={'required': "What do you wanna say?"},		

		)
class BadgeForm(forms.ModelForm):

#	def get_user(self, user):
#		self.user = user
#	def set_user(self, user):
#		global scout_username_list
#		query = User.objects.all()
#		troop = user.userprofile.troop
#		userprofile = UserProfile.objects.all()
#		selected_scouts = userprofile.filter(troop=troop)
#		for scout in selected_scouts:
#			username = str(scout.scout_username)

#			scout_username_list.append((username, username))


	
		
#		query = User.objects.filter(scout_username__username__in=display_list)

#	scout_username = forms.ChoiceField(choices=scout_username_list)

	class Meta:
		model = ScoutData
		fields = ('scout_username', 'Pioneer_Badge', 'Explorer_Badge', 'Adventurer_Badge', 'Proficiency_Badge', 'Other_Badge') 
		#comma is necessary because of tuple unpacking x,y = (1,2) - leaves it as a tuple

	#filters the accessible scouts
	def __init__(self, user=None, *args, **kwargs):
#		self.user = kwargs.pop("user")
		self.user = user

		super(BadgeForm, self).__init__(*args, **kwargs)
#		self.fields['scout_username'].queryset = UserProfile.objects.filter(troop='BC')
		self.fields['scout_username'].queryset = User.objects.filter(userprofile__troop=user.userprofile.troop, userprofile__role='Scout')


#	def clean(self):
#		cleaned_data = super().clean()
#		Pioneer_Badge = cleaned_data.get('Pioneer_Badge')
#		Explorer_Badge = cleaned_data.get('Explorer_Badge')
#		Adventurer_Badge = cleaned_data.get('Adventurer_Badge')
#
#		if '' in Pioneer_Badge and '' in Explorer_Badge and '' in Adventurer_Badge:
#			msg = "Please select at least 1 badge"
#			self.add_error('Pioneer_Badge', msg)
#			self.add_error('Explorer_Badge', msg)
#			self.add_error('Adventurer_Badge', msg)
'''
	user1 = User.objects.get(username ='user1')

	st_username_list=[
		(None, 'Choose a user'),
		(user1, 'user1'),
		(i, 'no progress'),
		]

	class BadgeForm(forms.ModelForm):
		def set_user(self, user):
			global st_username_list
			troop = user.userprofile.troop
			userprofile = UserProfile.objects.all()
			selected_st = userprofile.filter(troop=troop)
			for st in selected_st:
				username = str(st.st_username)
				st_username_list.append((username, username))
		st_username = forms.ChoiceField(choices=st_username_list)
		class Meta:
			model = stData
			fields = ('st_username', 'Pioneer_Badge', 'Explorer_Badge', 'Adventurer_Badge', 'Proficiency_Badge', 'Other_Badge') 
			#comma is necessary because of tuple unpacking x,y = (1,2) - leaves it as a tuple

	'''	