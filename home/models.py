from django.db import models
from django import forms

# Create your models here.
class ContactForm(forms.Form):
	subject_choices=[
	(None, 'Select'),
	('Pricing Query', 'Pricing'),
	('Feedback', "Feedback"),
	('Other', 'Other')
	]
	first_name = forms.CharField(required=True, 
		label='First Name:',
		error_messages={'required': 'Please enter your name'},
		)

	last_name = forms.CharField(required=True, 
		label='Last Name:',
		error_messages={'required': 'Please enter your name'},		
		)

	email = forms.EmailField(required=True,
		label='Email:',
		error_messages={'required': 'It helps to have your email'},		
)

	subject = forms.ChoiceField(choices=subject_choices, 
		label='Subject:',
		error_messages={'required': 'Please select subject'},
		)

	message = forms.CharField(required=True, 
		label='Message:', 
		widget=forms.Textarea,
		max_length='500',
		min_length='10',
		error_messages={'required': "Why do you want to contact us?"},		

		)

#$$$ magic!
''' 
import settings
 
class Sale(models.Model):
    def __init__(self, *args, **kwargs):
        super(Sale, self).__init__(*args, **kwargs)
 
        # bring in stripe, and get the api key from settings.py
        import stripe
        stripe.api_key = settings.STRIPE_API_KEY
 
        self.stripe = stripe
 
    # store the stripe charge id for this sale
    charge_id = models.CharField(max_length=32)
 
    # you could also store other information about the sale
    # but I'll leave that to you!
 
    def charge(self, price_in_cents, number, exp_month, exp_year, cvc):
        """
        Takes a the price and credit card details: number, exp_month,
        exp_year, cvc.
 
        Returns a tuple: (Boolean, Class) where the boolean is if
        the charge was successful, and the class is response (or error)
        instance.
        """
 
        if self.charge_id: # don't let this be charged twice!
            return False, Exception(message="Already charged.")
 
        try:
            response = self.stripe.Charge.create(
                amount = price_in_cents,
                currency = "usd",
                card = {
                    "number" : number,
                    "exp_month" : exp_month,
                    "exp_year" : exp_year,
                    "cvc" : cvc,
 
                    #### it is recommended to include the address!
                    #"address_line1" : self.address1,
                    #"address_line2" : self.address2,
                    #"daddress_zip" : self.zip_code,
                    #"address_state" : self.state,
                },
                description='Thank you for your purchase!')
 
            self.charge_id = response.id
 
        except self.stripe.CardError, ce:
            # charge failed
            return False, ce
 
        return True, response
'''
#an easier $$ trick
class Payments(models.Model):
	plan = models.CharField(max_length=50)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	troop = models.CharField(max_length=250)

	charge_id = models.CharField(max_length=234)