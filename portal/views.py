from django.shortcuts import render,redirect
from django.http import HttpResponse
from portal.forms import registrationform
from portal.models import Register
from django.contrib.auth.models import User
from django.core.mail import send_mail
from portalpro import settings
from django.contrib import messages

def register(request):
	if request.method=='POST':
		firstName = request.POST['firstName']
		emailId = request.POST['emailId']
		password = User.objects.make_random_password(length=8,allowed_chars="abcdefghijklmnopqrstuvwxyz1234567890@#$")	
		#password = request.POST['password']
		has_email = False
		try:
			Register.objects.get(emailId=emailId)
			has_email = True
		except Exception as e:
			pass
		if has_email :
			messages.warning(request,emailId+'   already exist, please login in Portal ')
		else:
			obj = Register(emailId=emailId,password=password)
			obj.save()
			subject = 'Reset your portal Password'
			body = 'Dear '+firstName+' \n Your Successfully registed in Portal. \n the Login URl is http://127.0.0.1:8000/login/ \n Username : '+ emailId +' \n This is your system generated Passcode : ' + password 
			receiver = request.POST['emailId']
			sender  = settings.EMAIL_HOST_USER
			send_mail(subject,body,sender,[receiver])
			return HttpResponse('Mail Sent to You Once .....')
	form = registrationform()
	return render(request,'portal/register.html',{'form':form})


def resetpassword(request):
	if request.method == 'POST':
		old = request.POST['oldPassword']
		new = request.POST['newPassword']
		confirm = request.POST['confirmPassword']
		obj = Register.objects.get(password=old)
		emailId = obj.emailId
		has_oldpass = False
		try:
			Register.objects.get(emailId=emailId,password=old)
			has_oldpass = True
		except Exception as e:
			pass
		if has_oldpass :
			if new == confirm:
				data = Register.objects.get(password=old,emailId=emailId)
				data.password = confirm
				data.save()
				return render(request,'portal/portal.html',{}) 
		else:
			messages.warning(request,'Invalid credintials ')
			return render(request,'portal/resetpassword.html')
	return render(request,'portal/resetpassword.html')

	
def login(request):
	if request.method == 'POST':
			emailId = request.POST['emailId']
			pwsd = request.POST['password']
			data = Register.objects.get(emailId=emailId)
			has_user = False
			try:
				Register.objects.get(emailId=emailId,password=pwsd)
				has_user = True
			except Exception as e:
				pass
			if has_user :
				return render(request,'portal/portal.html',{}) 
			else:
				print("Invalid credintials")
				messages.warning(request,'Invalid credintials ')
				return render(request,'portal/login.html',{})
	return render(request,'portal/login.html',{})


