from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from datetime import date
from django.utils.translation import gettext_lazy as _



from accounts.models import UserProfile, UserProfileManager, UserManager 
from leaders.models import ScoutData, ScoutDataManager
# Register your models here.

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

class ScoutDataAdmin(admin.ModelAdmin):
	list_display = (
		'scout_username', 'Pioneer_Badge', 'Explorer_Badge', 
		'Adventurer_Badge', 'Proficiency_Badge', 'Other_Badge', 'date'
		)

	def get_queryset(self, request):
		scout_display_list = []

		queryset = ScoutDataManager.get_queryset(self, request)
		queryset = queryset.order_by('-scout_username', '-Pioneer_Badge', '-Explorer_Badge',
		 '-Adventurer_Badge', '-Proficiency_Badge', '-Other_Badge')

		return queryset
admin.site.register(ScoutData, ScoutDataAdmin)

class UserProfileAdmin(admin.ModelAdmin):
	admin_objects = UserProfileManager()
	list_display = (
	'user', 'age')

	def user(self, obj):
		return obj.scout_username

	def age(self, obj):
		age = calculate_age(obj.date_of_birth)
		return age

	def get_queryset(self, request):
		scout_display_list = []

		queryset = UserProfileManager.get_queryset(self, request)

		return queryset
admin.site.register(UserProfile, UserProfileAdmin)

class UserCreateForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super(UserCreateForm, self).__init__(*args, **kwargs)
		self.fields['email'].required = False
		self.fields['email'].help_text = 'Prefered email to contact scout.'
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False
	verbose_name_plural = 'UserProfile'
	fk_name = 'scout_username'


#User Site
#Filters
class GroupListFilter(admin.SimpleListFilter):
	title = _('Role')
	parameter_name = 'group'

	def lookups(self, request, model_admin):
		return(
			('Leader', _('Leaders')), #LHS = value
			('Scouts', _('Scouts')) #RHS = human readable which is shown on screen
			)

	def queryset(self, request, queryset):
		#returns queryset. Get provided value by doing self.value()
		if self.value() == 'Leader':
			return queryset.filter(groups__name='Leader')
		if self.value() == 'Scouts':
			return queryset.filter(groups__name='Scouts')

class CustomUserAdmin(UserAdmin):
	#custom form
	add_form = UserCreateForm
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'email', 'password1', 'password2'),
		}),
	)
	#custom user view
	inlines = (UserProfileInline, )

	list_display = ('username', 
		'name', 'age',
		)

	def name(self, obj):
		name = "{} {}".format(obj.first_name, obj.last_name)
		return name

	def age(self, obj):
			age = calculate_age(obj.userprofile.date_of_birth)
			return age

	#Queryset -- getting all members of that troop
	def get_queryset(self, request):
		queryset = UserManager.get_queryset(self, request)
		return queryset


	#custom filter
	list_filter = (GroupListFilter,)

	#fieldsets
	fieldsets = (
		((None), {'fields': ('username', 'password')}),
		(('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
		(('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
										'groups', 'user_permissions')}),
		(('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

	leader_fieldsets = (
        ((None), {'fields': ('username', 'password')}),
        (('Personal'), {'fields': ('first_name', 'last_name', 'email')}),
        )





	#making it so leaders can only view  the fields within leaders_fieldset
	def get_fieldsets(self, request, obj=None):
		if request.user.groups.filter(name='Leader').exists() and not(request.user.is_superuser) and not(is_add_form(request)):
			return self.leader_fieldsets
		else:
			return super(CustomUserAdmin, self).get_fieldsets(request, obj=obj)

			#adding the userprofile stuff to the user create form
	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

#	def get_form(self, request, obj=None, **kwargs):
#		defaults ={'form': UserCreateForm}
#		if obj is None:
#			defaults['form'] = self.add_form
#		defaults.update(kwargs)
#		return super(CustomUserAdmin, self).get_form(request, obj, **defaults)


#url info
	#retrieves the url and see's if it says add at the end
	#if so, returns True, otherwise returns False
def is_add_form(request):
	path_info = request.META.get('PATH_INFO')
	last_path = str(path_info.split('/')[-2])
	if last_path == 'add':
		return True
	else:
		return False

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)