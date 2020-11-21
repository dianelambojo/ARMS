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

class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')		