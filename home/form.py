from django import forms
from datetime import datetime

def current_year():
	return int(datetime.now().year)

class StripeForm(forms.Form):
	stripe_token = forms.CharField()

class BTroopSignup(forms.Form):
	BasicTroop_id = forms.CharField(
		required=True, 
		label="Troop Name",
		min_length= 5,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Troop name should be a minimum of 5 characters long',

		}

		)
	BasicTroop_abr = forms.CharField(
		required=True,
		label="Troop Abreviation",
		max_length = 5,
		min_length=2,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Your abbreviation was less than 2 characters long and it should be between 2-5.',
		'max_length': 'Your abbreviation was more than 5 characters long and it should be between 2-5.',
		}
		)
	BasicTroop_fd_date = forms.IntegerField(
		required=True,
		label="Foundation Date",
		max_value = current_year(),
		min_value = 1908,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_value': 'You chose a year before scouts was originally founded!',
		'max_value': "You chose a year from the future! No more time travelling please." 
		}
		)

class PTroopSignup(forms.Form):
		PremTroop_id = forms.CharField(
		required=True, 
		label="Troop Name",
		min_length= 5,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Troop name should be a minimum of 5 characters long',

		}

		)
		PremTroop_abr = forms.CharField(
		required=True,
		label="Troop Abreviation",
		max_length = 5,
		min_length=2,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Your abbreviation was less than 2 characters long and it should be between 2-5.',
		'max_length': 'Your abbreviation was more than 5 characters long and it should be between 2-5.',
		}
		)
		PremTroop_fd_date = forms.IntegerField(
		required=True,
		label="Foundation Date",
		max_value = current_year(),
		min_value = 1908,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_value': 'You chose a year before scouts was originally founded!',
		'max_value': "You chose a year from the future! No more time travelling please." 
		}
		)

class PricingFormA(forms.Form):
		Test_ATroop_id = forms.CharField(
		required=True, 
		label="Troop Name",
		min_length= 5,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Troop name should be a minimum of 5 characters long',

		}

		)
		Test_ATroop_abr = forms.CharField(
		required=True,
		label="Troop Abreviation",
		max_length = 5,
		min_length=2,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Your abbreviation was less than 2 characters long and it should be between 2-5.',
		'max_length': 'Your abbreviation was more than 5 characters long and it should be between 2-5.',
		}
		)
		Test_ATroop_fd_date = forms.IntegerField(
		required=True,
		label="Foundation Date",
		max_value = current_year(),
		min_value = 1908,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_value': 'You chose a year before scouts was originally founded!',
		'max_value': "You chose a year from the future! No more time travelling please." 
		}
		)

		'''AOldMasterPassword = forms.CharField(
									help_text = 'An option to keep your old password upon renweing the membership. Not to be filled out if creating an account for your troop for the first time.',
									widget = forms.PasswordInput(attrs={'class':'has-popover', 
													'data-content':'help_text', 
													'data-placement':'right', 
													'data-container':'body'}),
									required = False,
									label= ' Previous Password: (Renewals only)',
									)'''


class PricingFormB(forms.Form):
		Test_BTroop_id = forms.CharField(
		required=True, 
		label="Troop Name",
		min_length= 5,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Troop name should be a minimum of 5 characters long',

		}

		)
		Test_BTroop_abr = forms.CharField(
		required=True,
		label="Troop Abreviation",
		max_length = 5,
		min_length=2,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Your abbreviation was less than 2 characters long and it should be between 2-5.',
		'max_length': 'Your abbreviation was more than 5 characters long and it should be between 2-5.',
		}
		)
		Test_BTroop_fd_date = forms.IntegerField(
		required=True,
		label="Foundation Date",
		max_value = current_year(),
		min_value = 1908,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_value': 'You chose a year before scouts was originally founded!',
		'max_value': "You chose a year from the future! No more time travelling please." 
		}
		)

		Test_BTroop_email = forms.EmailField(
			required=True,
			label="Email",
			error_messages={
			'required': "um... you left the field blank. Please don't do that again.",
			}

			)