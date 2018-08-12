
#in case user.userprofile.troop does not work
from accounts.models import UserProfile, UserProfileManager

from django.contrib.auth.models import User

#gets troop the scout is in
class UserProfileGetter():
		def Troop(request):
			user = request.user
			current_user_details = UserProfile.objects.all().filter(scout_username=user)
			troop = current_user_details.exclude(troop='')
			return troop
