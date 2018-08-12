from django.urls import path
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



from leaders.badge_requests import (
	SpecificBadgeRequestView_1,

	)
from leaders.views import (

	HomeView, 
	RequestBadgeQuantityView,
	SubmitedView,
	ScoutView,

	Badge_Report,
	Report_Quantity,
	testView,


)
from leaders import views



app_name="leaders"

urlpatterns = [
	path('', HomeView.as_view()
		, name='home'),

	path('badge_request_quantity', RequestBadgeQuantityView.as_view(), name="badge_request_quantity"),
	path('badge_request_quantity/<int:quantity>', SpecificBadgeRequestView_1.as_view(), name="specific_badge_request"),

	path('badge_request_quantity/success', SubmitedView.as_view(), name="redirect"),

	path('test', testView.as_view(), name="test"),
	path('badge_report_<int:month>', Badge_Report.as_view(), name="badge_report"),
	path('badge_report_quantity', Report_Quantity.as_view(), name="Report_Quantity"),

] + staticfiles_urlpatterns()