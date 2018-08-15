from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import EditProfileForm

from accounts.badge_views import Percentager, DataListRequest

from django.urls import reverse

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from accounts.models import UserProfile, UserProfileManager


def logout_view(request, **kwargs):
	return redirect('home_page:home')

# Create your views here

#home view
def home(request, **kwargs):
#	user_var = request.user
#	queryset = UserProfile.objects.filter(scout_username=user_var)
#	slug_name = get_object_or_404(queryset, slug=slug)
#	print (slug_name)
	slug = request.user.userprofile.troop
	pioneer_empty = False
	explorer_empty = False
	adventurer_empty = False

	#displays the percentage progress in each section
	pioneer_progress = Percentager.Pioneer(request)
	explorer_progress = Percentager.Explorer(request)
	adventurer_progress = Percentager.Adventurer(request)

	#get the badges for each section
	pioneer_badges = DataListRequest.Pioneer(request)
	explorer_badges = DataListRequest.Explorer(request)
	adventurer_badges = DataListRequest.Adventurer(request)

	#if it was actually empty
	if len(pioneer_badges) == 0:
		pioneer_empty = True
	elif len(explorer_badges) == 0:
		explorer_empty = True
	elif (adventurer_badges) == 0:
		adventurer_empty = True

	
	args = {'slug_arg': slug, 'user': request.user, 
	'pioneer_progress': pioneer_progress, 
	'explorer_progress':explorer_progress, 
	'adventurer_progress':adventurer_progress,
	'pioneer_badges': pioneer_badges,
	'explorer_badges': explorer_badges,
	'adventurer_badges':adventurer_badges,
	'pioneer_empty': pioneer_empty,
	'explorer_empty': explorer_empty,
	'adventurer_empty': adventurer_empty,
	}
	return render(request, 'accounts/home.html', args)




def view_profile(request, **kwargs):
	# a page so the scouts can see their profile
	slug = request.user.userprofile.troop
	Editform = EditProfileForm()
	Passform = PasswordChangeForm(user=request.user)

	args = {'user': request.user, 'slug_arg': slug,
	'Passform': Passform, 'Editform': Editform, 'error': False, 'success': False}

	if request.method == 'POST':
		Passform = PasswordChangeForm(data=request.POST, user=request.user)
		Eform = EditProfileForm(request.POST, instance=request.user)

		if Passform.is_valid():
			Passform.save()
			update_session_auth_hash(request, Passform.user)
			args['success'] = True
			

		elif Editform.is_valid():
			Editform.save()
			args['success'] = True
		elif not(Editform.is_valid) and not(Passform.is_valid):
			args['error'] = True


	return render(request, 'accounts/profile.html', args)

def edit_profile(request, **kwargs):
	#A page where they can edit some of their details, 
	# To-Do: refine it so only certain details are editable
	slug = request.user.userprofile.troop
	if request.method == 'POST':
		Eform = EditProfileForm(request.POST, instance=request.user)

		if Editform.is_valid():
			Editform.save()
			return redirect('accounts:view_profile', slug=slug)
	else:
		Editform = EditProfileForm()
		args = {'Editform': Editform}
	return render(request, 'accounts/edit_profile.html', args)


def change_password(request, **kwargs):
	slug = request.user.userprofile.troop
	if request.method == 'POST':
		Passform = PasswordChangeForm(data=request.POST, user=request.user)

		if Passform.is_valid():
			Passform.save()
			update_session_auth_hash(request, Passform.user)
			return redirect('accounts:view_profile', slug=slug)
		else:
			return redirect("accounts:change_password", slug=slug)
	else:
		Passform = PasswordChangeForm(user=request.user)
		args = {'Passform': Passform, 'slug':slug}

		return render(request, 'accounts/change_password.html', args)		
#badges
def view_pioneer(request, **kwargs):
	slug = request.user.userprofile.troop
	args = {'user': request.user, 'slug_arg': slug,}
	return render(request, 'accounts/pioneer.html', args)