from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .forms import *
from .models import *
import re
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


# 1 Makemigrations
# 2 Migrate
# 3 Createsuperuser for django admin
# 4 Go to register page 
# 5 Fill out details, password dpat tarong kay mo error sya
# 6 Check django admin if nasuod sya
# 7 Login, pero dle pa sya mo redirect sa page

def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('homepage_view')#redirect homepage not working
		else:
			messages.info(request, 'Username OR password is incorrect')
			
	context = {} 
	return render(request,'login.html',context)

def logoutUser(request):
	logout(request )
	return redirect ('login_view')


def registerPage(request):
	form = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(data=request.POST)
		print(form.is_valid())
		print(form.errors)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for '+user)

	context = {'form':form}
	return render(request,'register.html',context)


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
		# books = Books.objects.all()
		# authors = Author.objects.all()
		# context={
		# 	'books' : books,
		# 	'authors' : authors,
		# }
		# return render(request, 'homepage.html', context)
		return render(request, 'homepage.html')

	def post(self, request):
	# 	inputText = request.POST.get('searchBox')
	# 	print(inputText)
	# 	authors = Author.objects.all()
	# 	conn = mysql.connector.connect(
	# 		user="root", password="", host="127.0.0.1", database="arms_database")
		
	# 	cursor = conn.cursor()

	# 	cursor.execute("SELECT * from Books WHERE book_title=%s",[inputText])
	# 	books = cursor.fetchall()
	# 	print(books)
	# 	conn.close()

	# 	context={
	# 		'books' : books,
	# 		'authors' : authors,
	# 	}

	# 	return render(request, 'homepage.html', context)
		return render(request, 'homepage.html')

#sample custom pdf viewer
class PdfViewer(View):
	def get(self, request):
		return render(request, "pdfViewer.html")

class ProfileIndexView(View):
	def get(self, request):
		user = User.objects.all()
		#print(user)
		context = {
			'users' : user
		}

		return render(request, 'profile.html', context)

	def post(self,request):
		return render(request, 'addbook.html')	

class LandingPageIndexView(View):
	def get(self, request):
		return render(request, 'landingpage.html')


class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')

class AddBookIndexView(View):
	def get(self, request):
		#queryset
		booksQS = Books.objects.all()
		print(booksQS)
		#printing all items in books
		for item in booksQS:
			print("\t[Book ID: ",item.book_id,"]")
			print("\t[Title: ",item.book_title,"]")
			print("\t[Book Author ID: ",item.book_author_id,"]")
			print("\t[Book Cover: ",item.book_cover,"]")
			print("\t[File: ",item.book_file,"]")
			print("\t[Year: ",item.book_year,"]")
			print("\t[Tags: ",item.book_tags,"]")
			print("\t[Summary: ",item.book_summary,"]")
			print("\t[Category: ",item.book_category_no,"]")
			print("----------------------------------------\n")

			context={
			'books' : booksQS
			}
		return render(request, 'addbook.html')

	# def post(self, request):
	# 	form = BooksForm(request.POST, request.FILES)
	# 	if form.is_valid():
	# 		book_id = request.POST.get('book_id')
	# 		book_title = request.POST.get('book_title')
	# 		book_author_id = request.POST.get('book_author_id')
	# 		book_cover = request.FILES['book_cover']
	# 		book_file = request.FILES['book_file']
	# 		book_year = request.POST.get('book_year')
	# 		book_tags = request.POST.get('book_tags')
	# 		book_summary = request.POST.get('book_summary')
	# 		book_category_no = request.POST.get('book_category_no')
	# 		book_info = request.POST.get('book_info')
	# 		form = Books(book_id = book_id, book_title = book_title, book_author_id = book_author_id, book_cover = book_cover,
	# 			book_file = book_file, book_year = book_year, book_tags = book_tags, book_summary = book_summary, book_category_no = book_category_no, book_info = book_info)
	# 		form.save()
	# 		return HttpResponse('Book Saved!')
	# 	else:
	# 		print(form.errors)
	# 		return HttpResponse('Not Valid')