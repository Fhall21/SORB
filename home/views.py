
from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required

from home.form import StripeForm, BTroopSignup, PTroopSignup, PricingFormA, PricingFormB
from django.conf import settings
from django.contrib.auth.models import User

from home.models import ContactForm, Payments
from accounts.models import UserProfile #, GroupRecord fix 
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from scouts import settings
import stripe, bs4, time
'''
stripe_keys = {
	'secret_key': settings.STRIPE_TEST_SECRET_KEY,
	'publishable_key': settings.STRIPE_TEST_PUBLIC_KEY
}
stripe.api_key = stripe_keys['secret_key']
'''

def blank_field(packaged_errors):
	blank = False
	blank_arr = {}
	passed_list = []
	for i in range(0, len(packaged_errors)):
		for mini_i in range(0, len(packaged_errors[i][1])):
			if 'field blank' in packaged_errors[i][1][mini_i]:
				blank_arr[i] = True

	for el in range(0, len(blank_arr)):
		passed_list.append(blank_arr[el])
	if len(passed_list) == 3:
		blank = True
	return blank


def error_packaging(error):
	empty_l = []
	l_error = list(error)
	for i in range(0, len(list(error))):
		if 'Troop_id' in l_error[i]:
			key = 'Troop Name'
		elif 'Troop_abr' in l_error[i]:
			key = 'Troop Abbreviation'
		elif 'Troop_fd_date' in l_error[i]:
			key = 'Foundation Date'
		empty_l.append(list((key, error[l_error[i]])))
	return empty_l

class WelcomeView(TemplateView):
	template_name = 'home/home_page.html'

	def get(self, request):

		#to do
		#check if troop name is already in database, if so, retrieve its master login
		#else
		#Create a Master Login
		#Add Troop Name as a new troop within the database

		amount = request.session.get('amount', '0')
		signup = request.session.get('signup', False)
		email = request.session.get('contact_email', 'an incorrect email address')

		#clearing of session variables
		request.session['amount'] = 0
		request.session['email'] = ''
		request.session['signup'] = False
		args = {
		'key': settings.STRIPE_TEST_PUBLIC_KEY,
		'signup': signup,
		'amount': amount,
		'email': email
		}
		return render(request, self.template_name, args)

class OldPricingView(TemplateView):
	template_name = 'home/pricing.html'

	def get(self, request):
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
		args = {'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'form_b': BTroopSignup(), 'form_p': PTroopSignup()
		}
		return render(request, self.template_name, args)

	def post(self, request):
		form_pass_valid = False

		print ("POSTED")
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

#		print (request.form['text'])
		form_info_b = BTroopSignup(request.POST)
		form_info_p = PTroopSignup(request.POST)

		if form_info_b.is_valid():
			form_pass_valid = True
			request.session['Troop_id'] = form_info_b.cleaned_data['BasicTroop_id']
			request.session['Troop_abr'] = form_info_b.cleaned_data['BasicTroop_abr']
			request.session['Troop_fd_date'] = form_info_b.cleaned_data['BasicTroop_fd_date']

			amount = 1200

		elif form_info_p.is_valid():
			form_pass_valid = True

			request.session['Troop_id'] = form_info_p.cleaned_data['PremTroop_id']
			request.session['Troop_abr'] = form_info_p.cleaned_data['PremTroop_abr']
			request.session['Troop_fd_date'] = form_info_p.cleaned_data['PremTroop_fd_date']

			amount = 1600
			
		if form_pass_valid:
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
			
			r_amount = float((str(amount))[:-2] + "." + (str(amount)[-2:]))

			request.session['amount'] = r_amount 
			request.session['contact_email'] = contact_email	
			return redirect ('home_page:paid')
		else:
			#html list of errors

			#form b errors
			errors_p = form_info_p.errors
			error_list_p = error_packaging(errors_p)
			print ('form P Errors: \n' + str(error_list_p))

			#creates a dictionary where the key is a new key with a human readble name

			#form b errors
			errors_b = form_info_b.errors
			error_list_b = error_packaging(errors_b)
			print ('form B Errors: \n' + str(error_list_b))

			args = {'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'form_p': BTroopSignup(), 
			'form_b': PTroopSignup(), 
			'error': True,
			'error_b': error_list_b, 'error_p': error_list_p,
			}
			return render(request, self.template_name, args)

'''
class CheckOutView(TemplateView):
	stripe.api_key = settings.STRIPE_TEST_SECRET_KEY
	new_payment = Payments(
			plan = "Stadard")

	def get(self, request):
		payment.save()
		return redirect('home_page:home')

	def post(self, request):
		token = request.POST.get("stripeToken")
		try:
			charge  = stripe.Charge.create(
				amount = 1600,
				currency = "aud",
				source = token,
				description = "standard plan"
			)

		new_payment.charge_id = charge.id

		except stripe.error.CardError as ce:
			return False, ce
		
'''
class Contact(TemplateView):
	template_name = 'home/contactUs.html'

	def get(self, request):
		form = ContactForm()
		args = {'form': form}
		return render(request, self.template_name, args)

	def post(self, request):
		form = ContactForm()		
		args = {'form': form}

		form_info = ContactForm(request.POST)
		if form_info.is_valid():
			first_name = request.POST.get('first_name', '')
			last_name = request.POST.get('last_name', '')
			email = request.POST.get('email', '')
			subject = request.POST.get('subject', '')
			message = request.POST.get('message', '')

			# email the profile with contact info
			
#			template = get_template('contact_template.txt')
#			context = {
#			'first_name': first_name,
#			'last_name': last_name,
#			'email': email,
#			'subject': subject,
#			'message': message,
#			}
#			content = template.render(context)
#			email = EmailMessage(
#				"New contact form submission",
#				content,
#				subject +'',
#				['youremail@gmail.com'],
#				headers = {'Reply-To': email }
#			)
#			email.send()
			msg = 'You have a query from {} {}, \n {}'.format(first_name, last_name, message)
			send_mail(subject, msg, 'from@example.com', [email], fail_silently=False,) 

			args.update({'success':True})
		return render(request, self.template_name, args)
			
			#try send_mail if it does not work

class PricingView(TemplateView):
	template_name = 'home/pricing2.html'
	
	def get(self, request):
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

		args = {
			'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'formA': PricingFormA(), #Premium
			'formB': PricingFormB() #Basic
		}
		return render(request, self.template_name, args)
	def post(self, request):
		valid_form = False
		form_used = None
		stripe.api_key = settings.STRIPE_TEST_SECRET_KEY

#		print (request.form['text'])
		form_info_a = PricingFormA(request.POST)
		form_info_b = PricingFormB(request.POST)

		if form_info_b.is_valid():
			p_name = 'Basic'

			form_used = 'B'
			valid_form = True
			amount = 0000
			plan = stripe.Plan.retrieve("plan_DLIn5NDMMMdMHj")

			request.session['Troop_id'] = form_info_b.cleaned_data['Test_BTroop_id']
			request.session['Troop_abr'] = form_info_b.cleaned_data['Test_BTroop_abr']
			request.session['Troop_fd_date'] = form_info_b.cleaned_data['Test_BTroop_fd_date']
			contact_email = form_info_b.cleaned_data['Test_BTroop_email']

			print('Form B:')
			print (request.session.get('Troop_id', 'Nothing sorry'))

		elif form_info_a.is_valid():
			form_used = 'A'
			print ('form A')

			amount = 1600
			plan = stripe.Plan.retrieve("plan_DLIkKZNvTGqfCg")
			p_name = 'Premium'
			valid_form = True

			request.session['Troop_id'] = form_info_a.cleaned_data['Test_ATroop_id']
			request.session['Troop_abr'] = form_info_a.cleaned_data['Test_ATroop_abr']
			request.session['Troop_fd_date'] = form_info_a.cleaned_data['Test_ATroop_fd_date']
			print('Form A:')
			print (request.session.get('Troop_id', 'Nothing sorry'))			

#			to fix up later
			timestamp = (int(time.time()) + 120) 

			contact_email = request.POST['stripeEmail']

			customer = stripe.Customer.create(
				email=contact_email,
				source=request.POST['stripeToken'],
				api_key = settings.STRIPE_TEST_SECRET_KEY
				)
#			charge = stripe.Charge.create(
#				customer = customer.id,
#				amount=amount,
#				currency='aud',
#				)

			
			subscription = stripe.Subscription.create(
				customer=customer.id,
				items=[
					{
				    "plan": plan,
				    },
				  ],
				trial_period_days = 30,

				)
		if valid_form:

			r_amount = float((str(amount))[:-2] + "." + (str(amount)[-2:]))
			new_leader = None
			request.session['amount'] = r_amount 
			request.session['contact_email'] = contact_email
			request.session['signup'] = True	

			print (request.session['Troop_abr'])

			#Group Creation
			'''if not(GroupRecord.objects.filter(group=request.session['Troop_id']).exists()):
													new_group = GroupRecord(group=request.session['Troop_id'], 
														abbreviation=request.session['Troop_abr'], subscription=p_name)
													new_group.save() fix '''

			Master_username = 'Master' + str(request.session['Troop_abr'])
			request.session['username'] = Master_username
			created = User.objects.filter(username=Master_username).exists()
			print(created)
			Mast_pass = str(request.session['Troop_abr']) + str(request.session['Troop_fd_date'])
			if not(User.objects.filter(username=Master_username).exists()):
				#user creation
				new_leader = User.objects.create_user(username=Master_username, password=Mast_pass, is_staff = True)
				new_leader.save()

				#userprofile
#				UserProfile.objects.create(scout_username=new_leader, troop=new_group)
				new_leader.userprofile.scout_username = new_leader
				new_leader.userprofile.role = 'Leader'
				new_leader.userprofile.troop = str(request.session['Troop_abr'])
				new_leader.userprofile.save()
			#add staff status

			#send email with details
			to_list = []
			to_list.append(contact_email)
			reply_list = []
			reply_list.append('email.service@sorb.com.au')

			welcome_msg = 'Hey there! \nI am excited to have you as part of this! SORB aims to help reduce your stress when managing scout records and it provides a growing abundance of features to help you. To get started, here are your login details: \n'
			body_msg = 'Master username: {} \nMaster password: {} \n\n'.format(Master_username, Mast_pass)
			closing_msg = 'If you have any trouble working things out, or if you have any feedback, please reply directly to this email. \n\nWelcome, \nFelix Hall'
			msg = welcome_msg + body_msg + closing_msg
			email = EmailMessage (
				subject = 'Welcome to SORB!',
				body=msg,
				from_email='email.service@sorb.com.au',
				reply_to=reply_list,
				to=to_list,
				headers={'Content-Type': 'text/plain'})
			email.send()
			#send_mail(subject, msg, 'felix.p.hall@gmail.com', [contact_email], fail_silently=False,) 

			return redirect ('home_page:home')

		elif (not (valid_form)) or existing_credentials:
			#error_packaging packages error to be [['field', ['error1, 'error2]]]
			#blank_field finds if all fields are blank, returns True if they are
			#form b errors

		

			Aerrors = form_info_a.errors
			Aerror_list = error_packaging(Aerrors)
			A_Blank_test = blank_field(Aerror_list)
			print (Aerror_list)

			#creates a dictionary where the key is a new key with a human readble name

			#form b errors
			Berrors = form_info_b.errors
			Berror_list = error_packaging(Berrors)
			B_Blank_test = blank_field(Berror_list)

			if form_used == "B" and existing_credentials:
				Berror_list.append(['Authenticating the user', ['Username provided has already been used. Try slighty changing your details']])
			elif form_used == 'A' and existing_credentials:
				Aerror_list.append(['Authenticating the user', ['Username provided has already been used. Try slighty changing your details']])


			args = {
			'key': settings.STRIPE_TEST_PUBLIC_KEY,
			'formA': PricingFormA(),
			'formB': PricingFormB(),
			}

			if B_Blank_test and A_Blank_test:
				args['blank_error'] = True
			elif B_Blank_test and not A_Blank_test:
				args['Aerror'] = Aerror_list
				args['blank_A'] = True
			elif A_Blank_test and not B_Blank_test:
				args['Berror'] = Berror_list
				args['blank_B'] = True
			print ('Error')

		return render(request, self.template_name, args)
		#Unique constraint failed: accounts_userprofile.scout_username_id




		
class ChargeView(TemplateView):
	#the name of the template which will be rendered
	template_name = 'home/paid.html'
	def get(self, request):

		#to do
		#check if troop name is already in database, if so, retrieve its master login
		#else
		#Create a Master Login
		#Add Troop Name as a new troop within the database

		amount = request.session.get('amount', '0')
		email = request.session.get('contact_email', 'an incorrect email address')
		args = {
		'amount': amount,
		'email': email
		}
		return render(request, self.template_name, args)
