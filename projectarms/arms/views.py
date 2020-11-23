from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .forms import UserForm
from .models import *

# Create your views here.

class ArmsAdminView(View):
	def get(self, request):
		books = Books.objects.all()
		users = User.objects.all()
		context={
			'books' : books,
			'users' : users,
		}
		return render(request,'admindashboard.html', context)


class HomepageView(View):
	def get(self, request):
		books = Books.objects.all()
		authors = Author.objects.all()
		context={
			'books' : books,
			'authors' : authors,
		}
		return render(request, 'homepage.html', context)

	def post(self, request):
		return render(request, 'homepage.html')

class ProfileIndexView(View):
	def get(self, request):
		user = User.objects.all()

		context = {
			'users' : user
		}

		return render(request, 'profile.html')

class LandingPageIndexView(View):
	def get(self, request):
		return render(request, 'landingpage.html')

class LoginIndexView(View):
	def get(self, request):
		return render(request, 'login.html')

class RegisterIndexView(View):
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		form = UserForm(request.POST)

		if form.is_valid():
			
			user_id = request.POST.get("user_id")
			firstname = request.POST.get("firstname")
			lastname = request.POST.get("lastname")
			birthdate = request.POST.get("birthdate")
			gender = request.POST.get("gender")
			contact_number = request.POST.get("contact_number")
			password = request.POST.get("password")
			confirmpassword = request.POST.get("confirmpassword")

			form = User(user_id = user_id, firstname = firstname, lastname = lastname, birthdate = birthdate, gender = gender, contact_number = contact_number,
						password = password, confirmpassword = confirmpassword)
			form.save()

			return HttpResponse('Record saved!')			

class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')		