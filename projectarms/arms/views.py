from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .models import *

# Create your views here.

class ArmsAdminView(View):
	def get(self, request):
		books = Books.objects.all()
		users = User.objects.all()
		context={
			'books' : Books.objects.all(),
			'users' : User.objects.all()
		}
		return render(request,'admindashboard.html', context)


class HomepageView(View):
	def get(self, request):
		return render(request, 'homepage.html')

	def post(self, request):
		return render(request, 'homepage.html')

class ProfileIndexView(View):
	def get(self, request):
		return render(request, 'profile.html')

class LandingPageIndexView(View):
	def get(self, request):
		return render(request, 'landingpage.html')

class LoginIndexView(View):
	def get(self, request):
		return render(request, 'login.html')

class RegisterIndexView(View):
	def get(self,request):
		context={
			'title': 'Registration',
		}
		return render(request, 'arms/register.html', context)

	def post(self,request):
		form = UserForm(request.POST,request.FILES)
		if form.is_valid():
			user_id = request.POST.get("add-userid")
			password = request.POST.get("add-password")
			firstname = request.POST.get("add-firstname")
			lastname = request.POST.get("add-lastname")
 		  	email = request.POST.get("add-email")
  			birthdate = request.POST.get("add-birthdate")
  			contact_number =  request.POST.get("add-contact_number")

			form = User(user_id=user_id ,password=password,firstname=firstname, lastname=lastname, email=email,
        				birthdate=birthdate,contact_number=contact_number)
				form.save()

				return redirect('arms:index_view')			
			else:
				print(form.errors)
				return HttpResponse('not valid')


class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')		