from django.urls import path, re_path
from . import views

from accounts.badge_views import Pioneer, Explorer, Adventurer



app_name="accounts"

urlpatterns = [
	path('', views.home, name="home"), 
	#account authenticating
 	path('logout/', views.logout_view, {'template_name': 'accounts/logout.html'}, name='logout'),
	#profile details
	path('profile/', views.view_profile, name='view_profile'),
	path('profile/edit/', views.edit_profile, name="edit_profile"),
	#password details
	path('profile/password/', views.change_password, 
		name="change_password"),

	#badges
	path('pioneer-progress/', Pioneer.as_view(), name='pioneer_progress'),
	path('explorer-progress/', Explorer.as_view(), name='explorer_progress'),
	path('adventurer-progress/', Adventurer.as_view(), name='adventurer_progress'),

	] 