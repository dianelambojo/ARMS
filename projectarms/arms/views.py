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