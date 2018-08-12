from django.views.generic import TemplateView
from django.shortcuts import render, redirect, get_object_or_404


from home.feedbackForms import (

	BTroopSignup, PTroopSignup, 
	TestFormA, TestFormB,
	)
from django.conf import settings

from django.template.loader import get_template
import stripe

#Edited the simplifyed version by adding the stripe details
#then got the error "You cannot use a Stripe token more than once"
#I believe this is because I am trying to use the token to send over the details to stripe for both forms
#Would there then be another way I could do this without using it twice?

class indexWithStripe(TemplateView):
	template_name = 'home/index.html'
	def get(self, request):

		args = {
			'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'formA': TestFormA(),
			'formB': TestFormB()
		}
		return render(request, self.template_name, args)
	def post(self, request):
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

#		print (request.form['text'])
		form_info_a = TestFormA(request.POST)
		form_info_b = TestFormB(request.POST)
		if form_info_a.is_valid():
			amount = 1600
			contact_email = request.POST['stripeEmail']

			customer = stripe.Customer.create(
				email=contact_email,
				source=request.POST['stripeToken'],
				api_key = settings.STRIPE_TEST_SECRET_KEY
				)
			charge = stripe.Charge.create(
				customer = customer.id,
				amount=amount,
				currency='aud',
				description='Flask Charge'
				)
			request.session['text'] = form_info_a.cleaned_data['txt']
			print (request.session.get('text', 'Nothing sorry'))
			
			return redirect ('home_page:index')

		elif form_info_b.is_valid():
			amount = 1200
			contact_email = request.POST['stripeEmail']

			customer = stripe.Customer.create(
				email=contact_email,
				source=request.POST['stripeToken'],
				api_key = settings.STRIPE_TEST_SECRET_KEY
				)
			charge = stripe.Charge.create(
				customer = customer.id,
				amount=amount,
				currency='aud',
				description='Flask Charge'
				)
			request.session['text'] = form_info_b.cleaned_data['txt']
			print (request.session.get('text', 'Nothing sorry'))
			return redirect ('home_page:index')

		else:
			
			args = {
			'formA': TestFormA(),
			'formB': TestFormB()
			}
		return render(request, self.template_name, args)



#the following was a test to check if having 2 forms was the problem
#everything worked and the desired content got printed to the command line
class Test(TemplateView):
	template_name = 'home/index.html'
	def get(self, request):
		args = {
			'formA': TestFormA(),
			'formB': TestFormB()
		}
		return render(request, self.template_name, args)
	def post(self, request):

#		print (request.form['text'])
		form_info_a = TestFormA(request.POST)
		form_info_b = TestFormB(request.POST)
		if form_info_a.is_valid():
			request.session['text'] = form_info_a.cleaned_data['txt']
			print (request.session.get('text', 'Nothing sorry'))
			
			return redirect ('home_page:home')

		elif form_info_b.is_valid():
			request.session['text'] = form_info_b.cleaned_data['txt']
			print (request.session.get('text', 'Nothing sorry'))
			return redirect ('home_page:home')

		else:
			
			args = {
			'formA': TestFormA(),
			'formB': TestFormB()
			}
		return render(request, self.template_name, args)


#a function which changes the error dictionary to a list which is esaier to render
#from dictionary {key:[value]} to --> [[key, [value]]
def error_packaging(error):
	empty_l = []
	l_error = list(error)
	for i in range(0, len(list(error))):
		if l_error[i] == 'Troop_id':
			key = 'Troop Name'
		elif l_error[i] == 'Troop_abr':
			key = 'Troop Abbreviation'
		elif l_error[i] == 'Troop_fd_date':
			key = 'Foundation Date'
		empty_l.append(list((key, error[l_error[i]])))
	return empty_l


class PricingView(TemplateView):
	template_name = 'home/pricing.html'

	def get(self, request):
		#stripe details
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
		args = {'key': settings.STRIPE_TEST_PUBLIC_KEY,
		#forms. B represents Basic Plan, P represents Premium Plan
			'form_b': BTroopSignup(), 'form_p': PTroopSignup()
		}
		return render(request, self.template_name, args)

	#Managing the post request
	def post(self, request):
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

		#retrieving the forms and their data
		form_info_b = BTroopSignup(request.POST)
		form_info_p = PTroopSignup(request.POST)

		#if Basic form had been completed -- WORKS PERFECTLY
		if form_info_b.is_valid():
			#retreiving the form details and setting them to a variable to be retreived later
			request.session['Troop_id'] = form_info_b.cleaned_data['Troop_id']
			request.session['Troop_abr'] = form_info_b.cleaned_data['Troop_abr']
			request.session['Troop_fd_date'] = form_info_b.cleaned_data['Troop_fd_date']

			#stripe checkout submition details
			amount = 1200
			contact_email = request.POST['stripeEmail']

			customer = stripe.Customer.create(
				email=contact_email,
				source=request.POST['stripeToken'],
				api_key = settings.STRIPE_TEST_SECRET_KEY
				)
			charge = stripe.Charge.create(
				customer = customer.id,
				amount=amount,
				currency='aud',
				description='Flask Charge'
				)
			#making the amount a human readable integer to display to the customer later
			r_amount = float((str(amount))[:-2] + "." + (str(amount)[-2:]))
			
			request.session['amount'] = r_amount 
			request.session['contact_email'] = contact_email
			#redirecting them to the confirmation page	
			return redirect ('home_page:paid')

		#else if Premium form had been completed -- THIS IS THE FORM I AM HAVING ISSUES WITH
		elif form_info_p.is_valid():
			#retreiving the form details and setting them to a variable to be retreived later
			request.session['Troop_id'] = form_info_p.cleaned_data['Troop_id']
			request.session['Troop_abr'] = form_info_p.cleaned_data['Troop_abr']
			request.session['Troop_fd_date'] = form_info_p.cleaned_data['Troop_fd_date']

			#stripe checkout submition details
			amount = 1600
			contact_email = request.POST['stripeEmail']

			customer = stripe.Customer.create(
				email=contact_email,
				source=request.POST['stripeToken'],
				api_key = settings.STRIPE_TEST_SECRET_KEY
				)
			charge = stripe.Charge.create(
				customer = customer.id,
				amount=amount,
				currency='aud',
				description='Flask Charge'
				)
			
			#making the amount a human readable integer to display to the customer later
			r_amount = float((str(amount))[:-2] + "." + (str(amount)[-2:]))

			request.session['amount'] = r_amount 
			request.session['contact_email'] = contact_email	
			#redirecting them to the confirmation page	
			return redirect ('home_page:paid')
		else:
			#this is where the form errors are retrieved and the page is reloaded with them

			#form p errors
			errors_p = form_info_p.errors
			#error packaging changes the dictionary to a list (view above for more details)
			error_list_p = error_packaging(errors_p)

			#form b errors
			errors_b = form_info_b.errors
			#error packaging changes the dictionary to a list (view above for more details)
			error_list_b = error_packaging(errors_b)

			args = {'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'form_p': BTroopSignup(), 
			'form_b': PTroopSignup(), 
			'error': True,
			'error_b': error_list_b, 'error_p': error_list_p,
			}
		return render(request, self.template_name, args)


class ChargeView(TemplateView):
	#the name of the template which will be rendered
	template_name = 'home/paid.html'
	def get(self, request):

		#retrieve the details submitted
		amount = request.session.get('amount', '0')
		email = request.session.get('contact_email', 'an incorrect email address')
		args = {
		'amount': amount,
		'email': email
		}
		#rendering the template to inform the customer of what they have paid
		#as well as informing them which email the confirmation email was sent to -- to do
		return render(request, self.template_name, args)