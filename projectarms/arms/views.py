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