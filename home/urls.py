from django.urls import include, path
from django.contrib import admin

from home.views import (
	WelcomeView, 
	PricingView, 
	Contact, 
#	SubscribeView, 
#	SuccessView,
#	index,
	ChargeView,

	)


app_name='home_page'

urlpatterns = [
	path('', WelcomeView.as_view(), name='home'),
	path('pricing/', PricingView.as_view(), name='pricing'),
#	path('pricing/payment', include('djstripe.urls', namespace="djstripe")),


#	path('pricing/checkout', CheckOutView.as_view(), name='checkout'),
	path('contact-us/', Contact.as_view(), name='contact'),
#	path('thank_you/', SuccessView.as_view(), name='thank_you'),
#	path('subscribe/', SubscribeView.as_view(), name='subscribe'),

	path('pricing/paid/', ChargeView.as_view(), name='paid'),
]