from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .forms import *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.db.models import Count
import datetime
from django.core.paginator import Paginator, EmptyPage
from itertools import chain

# Create your views here.


# 1 Makemigrations
# 2 Migrate
# 3 Createsuperuser for django admin
# 4 Go to register page 
# 5 Fill out details, password dpat tarong kay mo error sya
# 6 Check django admin if nasuod sya
# 7 Login, pero dle pa sya mo redirect sa page

#Pede nani idelete if dle gamiton ang login.html
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			# pass the name of the user to the base.html navbar
			request.session['username'] = username
			if request.user.is_superuser:
				return redirect('arms:arms_admin_view')
			else:
				return redirect('arms:homepage_view')
		else:
			messages.info(request, 'Username OR password is incorrect')
			
	context = {} 
	return render(request,'login.html',context)

def logoutPage(request):
	logout(request)
	return redirect('arms:landingpage_view')

def registerPage(request):
	form = CreateUserForm()
	
	if request.method == 'POST':
		form = CreateUserForm(data=request.POST)
		# print(form.is_valid())
		# print(form.errors)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was created for '+user)
			return redirect('arms:login_view')

	context = {'form':form}
	return render(request,'register.html',context)

# pagination 
def pageResults(request, x):
	p = Paginator(x,20)
	page_num = request.GET.get('page', 1)
	try:
		page = p.page(page_num)
	except:
		page = p.page(1)

	return page

#By category searched of all books function
def category_search(request, searched):
	arr = ['Research','Journal','Filipiniana','Engineering','ComputerScience','InformationTechnology','Business','Architecture']
	length = len(arr)
	i=0
	searched = searched
	while i<length:
		if searched == arr[i]:
			ctgy = Category.objects.get(book_category = searched)
			# for c in ctgy:
			books = Books.objects.filter(Q(book_category_no_id=ctgy.book_category_no))
			authors = Author.objects.all()
			category = Category.objects.all()
			context={
				'authors' : authors,
				# 'books' : books,
				'books' : pageResults(request, books),
				'search' : searched,
				'category' : category,
			}
			return render(request, 'results.html', context)
		else:
			i+=1

	return render(request, 'results.html', {'search' : searched})	

def author_category_search(request, searched, param):
	searched = searched
	param = param
	authors = Author.objects.filter(Q(firstname__icontains=searched) & Q(lastname__icontains=param))
	for author in authors:
		books = Books.objects.filter(book_author_id=author.book_author_id)
		category = Category.objects.all()
		x = Author.objects.all()
		context={
			'search' : searched + ' ' + param,
			# 'books' : page,
			'books' : pageResults(request, books),
			'authors' : x,
			'category' : category,
		}
		return render(request, 'results.html', context)

	# return category_search(request, searched)
	return render(request, 'results.html', {'search' : searched + ' ' + param})

def author_search(request, search):
	search = search 
	category = Category.objects.all()
	x = Author.objects.all()
	authors = Author.objects.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search))
	for author in authors:
		# if the author is found then it will proceed to search for the book that was written by the author
		books = Books.objects.filter(book_author_id=author.book_author_id)		
		# p = Paginator(books,20)
		# page_num = request.GET.get('page', 1)
		# try:
		# 	page = p.page(page_num)
		# except:
		# 	page = p.page(1)

		context={
			'search' : search,
			# 'books' : page,
			'books' : pageResults(request, books),
			'authors' : x,
			'category' : category,
		}
		return render(request, 'results.html', context)

	context={
		'search' : search,
		'authors' : x,
		'category' : category,
	}
	return render(request, 'results.html', context)

def bookTitle_search(request,search):
	search = search
	books = Books.objects.filter(Q(book_title__icontains=search) | Q(book_year__icontains=search))
	for book in books:
		# authors = Author.objects.filter(Q(book_author_id=book.book_author_id_id))
		category = Category.objects.all()
		authors = Author.objects.all()
		context={
			'search' : search,
			# 'books' : books,
			'books' : pageResults(request, books),
			'authors' : authors,
			'category' : category,
		}

		return render(request, 'results.html', context)

	# if the user tries to search using the authors first or last name
	return author_search(request, search) 

class ArmsAdminView(View):
	def get(self, request):
		books = Books.objects.all()
		users = User.objects.all()
		context={
			'books' : books,
			'users' : users,
		}
		return render(request,'admindashboard.html', context)

	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdateUser' in request.POST:	
				print('update profile button clicked')
				userid = request.POST.get("userid")
				username = request.POST.get("username")			
				firstname = request.POST.get("firstname")
				lastname = request.POST.get("lastname")
				email = request.POST.get("email")
				
				update_user = User.objects.filter(id = userid)
				update_user.update(username=username,first_name=firstname,last_name=lastname,email=email)
				
				print(update_user)
				print('profile updated')

			elif 'btnDeleteUser' in request.POST:	
				print('delete button clicked')
				userid = request.POST.get("userid")
				delete_user = User.objects.filter(id=userid)
				delete_user.delete()
				print('record deleted')

		return redirect('arms:arms_admin_view')

class HomepageView(View):
	def get(self, request):
		if request.method == 'GET':
			search = request.GET.get('search')
			if search:
				# if the user tries to search using the book title or year 
				return bookTitle_search(request,search)
			
			#call search by category function 
			searched = request.GET.get('searched')
			print(searched)
			param = request.GET.get('param')
			if searched is not None:
				if param is not None:
					return author_category_search(request, searched, param)
				else:
					return category_search(request, searched)

			#if not search/searched
			else:
				# new releases within the month of the year (more or less): days is disregarded
				today = datetime.date.today()
				books = Books.objects.filter(date_added__year=today.year, date_added__month=today.month)
				print(books)
				authors = Author.objects.all()
				category = Category.objects.all()
				context={
					'books' : books,
					'authors' : authors,
					'category' : category,
				}
				return render(request, 'homepage.html', context)
		#if request.method != GET else
		else:
			return render(request, 'homepage.html')			

class ProfileIndexView(View):
	def get(self, request):
		user = User.objects.all()
		books = Books.objects.all()
		bookRead = Books.objects.all()
		authors = Author.objects.all()
		#print(user)
		context = {
			'users' : user,
			'books' : books,
			'authors' : authors,
			'bookRead' : bookRead,
			
		}

		return render(request, 'profile.html', context)

	def post(self, request):
		if request.method == 'POST':
			print('hello')
			if 'btnUpdate' in request.POST:
				print('update profile button clicked')
				sid = request.POST.get("user-id")
				username = request.POST.get("username")			
				first_name = request.POST.get("first_name")
				last_name = request.POST.get("last_name")
				email = request.POST.get("email")

				update_user = User.objects.filter(id = sid).update(username=username,first_name=first_name,last_name=last_name,email=email)

				print(update_user)
				print('profile updated')

			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				sid = request.POST.get("book-id")
				print(sid)
				# book = Books.objects.filter(book_id = sid).delete()
				book = Books.objects.filter(book_id = sid).update(is_deleted=1)
				# author = Author.objects.filter(book_author_id = sid).delete()
				# form = Books.objects.filter(book_id = sid)
				print('record deleted')	



		return render(request, 'profile.html')
	# def post(self,request):
	# 	return render(request, 'addbook.html')	

class LandingPageIndexView(View):
	def get(self, request):
		return render(request, 'landingpage.html')

	def post(self,request):
		# if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				# pass the name of the user to the base.html navbar
				request.session['username'] = username
				if request.user.is_superuser:
					return redirect('arms:arms_admin_view')
				else:
					return redirect('arms:homepage_view')
			else:
				messages.info(request, 'Username OR password is incorrect')
				
			context = {} 
			return render(request,'homepage.html',context)


class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')

class AddBookIndexView(View):
	def get(self, request):
		#queryset
		booksQS = Books.objects.all()
		authorsQS = Author.objects.all()
		categoryQS = Category.objects.all()
		print(authorsQS)
		print(categoryQS)
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

	def post(self, request):
	 	form = BooksForm(request.POST, request.FILES)
	 	# book_author_id = Author.objects.get('book_author_id')
	 	# book_category_no = Author.objects.get('book_category_no_id')
	 	if form.is_valid():
	 		# book_id = request.POST.get('book_id')
	 		#book_author_id = request.POST.get('book_author_id')
	 		
	 		book_category = request.POST.get('book_category')
	 		
	 		firstname = request.POST.get('Firstname')
	 		lastname = request.POST.get('Lastname')
	 		author = Author.objects.filter(Q(firstname__icontains = firstname) & Q(lastname__icontains = lastname))
	 		if author:
	 			print(author)
	 			# author_id = author.book_author_id
	 			# print(author_id)
	 			# form = Books(book_author_id=author_id)
	 		else:
	 			# Author.objects.create(
	 			# 	firstname = firstname, 
	 			# 	lastname = lastname
	 			# )
	 			form = AuthorForm(firstname=firstname, lastname=lastname)
	 			form.save()
	 		#book_author_id = Author.objects.filter(book_author_id=book_author_id)
	 		
	 		category = Category.objects.filter(Q(book_category__icontains = book_category))
	 		if category:
	 			print(category)
	 		else:
	 			# Category.objects.create(
	 			# 	book_category = book_category
	 			# )
	 			form = CategoryForm(book_category= book_category)
	 			form.save()

 			author = Author.objects.filter(Q(firstname__icontains = firstname) & Q(lastname__icontains = lastname))
 			# print(author.book_author_id)
 			category = Category.objects.filter(Q(book_category__icontains = book_category))
 			# print(category.book_category_no)

 			# x = chain(author, category)
 			for a in author:
 				print(a.book_author_id)
 				for c in category:
 					print(c.book_category_no)
 					book_title = request.POST.get('book_title')
			 		book_cover = request.FILES.get('book_cover')
			 		book_file = request.FILES.get('book_file')
			 		book_year = request.POST.get('book_year')
			 		book_tags = request.POST.get('book_tags')
			 		book_summary = request.POST.get('book_summary')
			 		# book_info = request.POST.get('book_info')
			 		form = Books(book_title = book_title, book_author_id = Author.objects.get(book_author_id = a.book_author_id), book_cover = book_cover,
			 			book_file = book_file, book_year = book_year, book_summary = book_summary, book_category_no = Category.objects.get(book_category_no = c.book_category_no),
			 			is_bookmarked = 0, is_downloaded = 0, is_read = 0, is_deleted = 0)

			 		# form = Books(book_id = book_id, book_title = book_title, book_author_id = book_author_id, book_cover = book_cover,
			 			# book_file = book_file, book_year = book_year, book_tags = book_tags, book_summary = book_summary, book_category_no = book_category_no, book_info = book_info)
			 		form.save()
			 		return HttpResponse('Book Saved!')
		 	# else:
		 	# 	return HttpResponse('Not Saved!')
	 	else:
	 		print(form.errors)
	 		return HttpResponse('Not Valid')
