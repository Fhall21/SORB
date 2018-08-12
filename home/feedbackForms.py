from django import forms
from datetime import datetime

def current_year():
	return int(datetime.now().year)

class BTroopSignup(forms.Form):
	Troop_id = forms.CharField(
		required=True, 
		label="Troop Name",
		min_length= 5,
		error_messages={
		'required': "um... you left the field blank. Please don't do that again.",
		'min_length': 'Troop name should be a minimum of 5 characters long',

		}

		)
	Troop_abr = forms.CharField(
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
	Troop_fd_date = forms.IntegerField(
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

class PTroopSignup(BTroopSignup):
	pass

class TestFormA(forms.Form):
	txt = forms.CharField(
				required=True, 
		label="Text Field",
		)

class TestFormB(TestFormA):
	pass