import datetime
from .forms import *
from .models import *
from .forms import CreateUserForm
from itertools import chain
from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q, Count
from django.core.paginator import Paginator, EmptyPage
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
import pyttsx3
import speech_recognition as sr 
# import xlrd
# import mysql.connector

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
			return redirect('arms:landingpage_view')

	context = {'form':form}
	return render(request,'register.html',context)
def logoutPage(request):
	logout(request)
	return redirect('arms:landingpage_view')

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
			print(ctgy)
			# for c in ctgy:
			books = Books.objects.filter(Q(book_category_id=ctgy.book_category_no))
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
	authors = Author.objects.get(Q(firstname__icontains=searched) & Q(lastname__icontains=param))
	# for author in authors:
	if authors:
		books = Books.objects.filter(book_author_id=authors.book_author_id)
		category = Category.objects.all()
		x = Author.objects.all()
		context={
			'search' : searched + ' ' + param + "'s Works",
			'books' : pageResults(request, books),
			'authors' : x,
			'category' : category,
		}
		return render(request, 'results.html', context)
	else:
		# return category_search(request, searched)
		return render(request, 'results.html', {'search' : searched + ' ' + param + "'s Works"})

def author_search(request, search):
	search = search 
	category = Category.objects.all()
	x = Author.objects.all()
	authors = Author.objects.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search))
	for author in authors:
		# if the author is found then it will proceed to search for the book that was written by the author
		books = Books.objects.filter(book_author_id=author.book_author_id)		
		context={
			'search' : search,
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

def bookTitle_search(request, search):
	print(search)
	search = search
	books = Books.objects.filter(Q(book_title__icontains=search) | Q(book_year__icontains=search))
	if books:
		print('it got in')
		print(books)
		category = Category.objects.all()
		authors = Author.objects.all()
		context={
			'search' : search,
			'books' : pageResults(request, books),
			'authors' : authors,
			'category' : category,
		}
		return render(request, 'results.html', context)
	else:
		# if the user tries to search using the authors first or last name
		return author_search(request, search) 

def newReleases(request):
	# new releases within the month of the year (more or less): days is disregarded
	today = datetime.date.today()
	books = Books.objects.filter(date_added__year=today.year, date_added__month=today.month)
	authors = Author.objects.all()
	category = Category.objects.all()
	context={
		'books' : books,
		'authors' : authors,
		'category' : category,
	}
	return render(request, 'homepage.html', context)

def count (request):
	#is_read = 0
	#for read in range(len(readBooks)):
		#if readBooks[read] == to_find:
			#is_read += 1
	#return is_read

	readBooks = Books.objects.filter(is_read= '1').count()

	context = {
		'readBooks': readBooks
	}
	print(readBooks)

def speak(audio): 
      
    engine = pyttsx3.init() 
    # current value of engine property
    voices = engine.getProperty('voices') 
      
    # [0] = Male voice
    # [1] = Female voice 
    engine.setProperty('voice', voices[1].id) 
      
    # Method for the speaking of the the assistant 
    engine.say(audio)   
      
    # Blocks while processing all the currently 
    # queued commands 
    engine.runAndWait()


def Take_query(request): 
    while(True): 
        query = takeCommand(request).lower()

        if "hey walter" in query: 
            Hello(request)

        elif "search" in query:
        	speak("For searching of reading materials, you could directly say the book title, author or year.")

        elif "thank you" in query: 
            speak("My pleasure. Call me if you need anything.") 
            break

        elif query:
        	search = query
        	speak("here are the results for" + search)
        	return bookTitle_search(request, search)
          
def takeCommand(request):
    r = sr.Recognizer() 

    with sr.Microphone() as source: 
        print('Listening')
          
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        try: 
            print("Recognizing")
            Query = r.recognize_google(audio, language='en') 
            print("the command is printed=", Query)

        except Exception as e: 
            print(e) 
            speak("I'm sorry, I didn't get that. Please say it again.")
            takeCommand(request)

        return Query

def Hello(request): 
    speak("Hi, I am Walter , your library assistant. What do you want to search?")

class ArmsAdminView(View):
	#@staff_member_required(redirect_field_name='next', login_url='arms:landingpage_view')#If the user is logged in,is a staff member (User.is_staff=True),and is active (User.is_active=True),execute the view normally.
	def get(self, request):
		books = Books.objects.select_related('book_author', 'book_category').filter(is_deleted=False).all()
		#bookcategory= Books.objects.get(book_category_id)
		users = User.objects.all()
		#authors = Author.objects.all()
		#category = Category.objects.all() #get(pk=9) #filter(book_category_no=bookcategoryno)
		Totalbooks = Books.objects.filter(is_deleted=False).count()
		Totalusers = User.objects.count()
		context={
			'books' : books,
			'users' : users,
		#	'authors' : authors,
		#	'category' : category,
			'Totalbooks' : Totalbooks,
			'Totalusers' : Totalusers,
		}
		return render(request,'admindashboard.html', context)
	
	#@staff_member_required(redirect_field_name='next', login_url='arms:landingpage_view')
	def post(self, request):
		if request.method == 'POST':	
			if 'btnUpdateUser' in request.POST:	
				print('update user profile button clicked')
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
				print('delete user button clicked')
				userid = request.POST.get("userid")
				delete_user = User.objects.filter(id=userid)
				delete_user.delete()
				print('record deleted')

			elif 'btnUpdateBook' in request.POST:	
				print('update book button clicked')
				bookid = request.POST.get("bookid")
				booktitle = request.POST.get("booktitle")
				bookyear = request.POST.get("bookyear")
				booksummary = request.POST.get("booksummary")
				booktags = request.POST.get("booktags")

				bookcategoryno = request.POST.get("bookcategoryno")
				bookcategory = request.POST.get("bookcategory")

				authorid = request.POST.get("authorid")
				authorfname = request.POST.get("authorfname")
				authorlname = request.POST.get("authorlname")
				authoremail = request.POST.get("authoremail")
				authorbdate = request.POST.get("authorbdate")
				authorgender = request.POST.get("authorgender")

				update_book = Books.objects.filter(book_id = bookid)
				update_book.update(book_title = booktitle, book_year=bookyear, book_summary=booksummary, book_tags=booktags)

				update_category = Category.objects.filter(book_category_no=bookcategoryno)
				update_category.update(book_category=bookcategory)

				update_author = Author.objects.filter(book_author_id=authorid)
				update_author.update(firstname=authorfname, lastname=authorlname, email=authoremail, birthdate=authorbdate, gender=authorgender)

			elif 'btnDeleteBook' in request.POST:	
				print('delete book button clicked')
				bookid = request.POST.get("bookid")

				delete_book = Books.objects.filter(book_id=bookid)
				delete_book.update(is_deleted=True)
				print('record deleted')

		return redirect('arms:arms_admin_view')


class HomepageView(View):
	def get(self, request):
		if request.method == 'GET':
			search = request.GET.get('search')
			if search:
				# if the user tries to search using the book title or year 
				return bookTitle_search(request,search)
			#search by category  
			searched = request.GET.get('searched')
			param = request.GET.get('param')
			if searched is not None:
				if param is not None:
					return author_category_search(request, searched, param)
				else:
					return category_search(request, searched)
			#display new added books 
			else:
				return newReleases(request)
		else:
			return render(request, 'homepage.html')	

	def post(self,request):
		if request.method == "POST":
			if 'mic' in request.POST:
				Hello(request)
				return Take_query(request)
			elif 'read' in request.POST:
				idnum = request.POST.get('idnum')
				form = Books.objects.get(book_id=idnum)
				form.is_read = 1
				form.readCount += 1
				form.save()

				search = request.GET.get('search')
				if search:
					return bookTitle_search(request,search)
				searched = request.GET.get('searched')
				param = request.GET.get('param')
				if searched is not None:
					if param is not None:
						return author_category_search(request, searched, param)
					else:
						return category_search(request, searched)
				else:
					return newReleases(request)
			elif 'downLoad' in request.POST:
				idnum = request.POST.get('idnum')
				form = Books.objects.get(book_id=idnum)
				form.is_downloaded = 1
				form.downloadCount += 1
				form.save()

				search = request.GET.get('search')
				if search:
					return bookTitle_search(request,search)
				searched = request.GET.get('searched')
				param = request.GET.get('param')
				if searched is not None:
					if param is not None:
						return author_category_search(request, searched, param)
					else:
						return category_search(request, searched)
				else:
					return newReleases(request)
			elif 'bookmark' in request.POST:
				idnum = request.POST.get('idnum')
				form = Books.objects.get(book_id=idnum)
				form.is_bookmarked = 1
				form.bookmarkCount += 1
				form.save()

				search = request.GET.get('search')
				if search:
					return bookTitle_search(request,search)
				searched = request.GET.get('searched')
				param = request.GET.get('param')
				if searched is not None:
					if param is not None:
						return author_category_search(request, searched, param)
					else:
						return category_search(request, searched)
				else:
					return newReleases(request)
		else:
			return render(request, 'homepage.html')	

class ProfileIndexView(View):
	def get(self, request):
		user = User.objects.all()
		books = Books.objects.all()
		authors = Author.objects.all()
		context = {
			'users' : user,
			'books' : books,
			'authors' : authors,
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
				book = Books.objects.filter(book_id = sid)
				book.update(is_deleted=1)
				# author = Author.objects.filter(book_author_id = sid).delete()
				# form = Books.objects.filter(book_id = sid)
				print('record deleted')	
		return redirect('arms:profile_view')

	# def post(self,request):
	# 	message_count = User.objects.filter(username='username').count()
	# 	return render(request, 'addbook.html')	

class LandingPageIndexView(View):
	def get(self, request):
		return render(request, 'landingpage.html')

	def post(self,request):
		# if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)
			print(user)

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
				
			# context = {} 
			return render(request, 'landingpage.html')


class AboutUsIndexView(View):
	def get(self, request):
		return render(request, 'aboutUsPage.html')

class AddBookIndexView(View):
	def get(self, request):
		return render(request, 'addBook.html')

	def post(self, request):
		form = AuthorForm(request.POST, request.FILES)
		if form.is_valid():
	 		bookcategory = request.POST.get('book_category')
	 		print(bookcategory)
	 		first_name = request.POST.get('firstname')
	 		last_name = request.POST.get('lastname')
	 		email = request.POST.get('email')
	 		birthdate = request.POST.get('birthdate')
	 		author = Author.objects.filter(Q(firstname__icontains = first_name) & Q(lastname__icontains = last_name))
	 		if author:
	 			print('.')
	 		else:
	 			form = Author(firstname = first_name, lastname = last_name, birthdate = birthdate, email = email)
	 			form.save()

	 		category = Category.objects.filter(Q(book_category__icontains = bookcategory))
	 		if category:
	 			print(',')
	 		else:
	 			# form = CategoryForm(request.POST)
	 			form = Category(book_category = bookcategory)
	 			form.save()

 			# author = Author.objects.filter(Q(firstname__icontains = firstname) & Q(lastname__icontains = lastname))
 			# category = Category.objects.filter(Q(book_category__icontains = book_category))

 			for a in author:
 				for c in category:
 					bookTitle = request.POST.get('book_title')
			 		bookCover = request.FILES.get('book_cover')
			 		bookFile = request.FILES.get('book_file')
			 		bookYear = request.POST.get('book_year')
			 		bookTags = request.POST.getlist('book_tags')
			 		print(bookTags)
			 		bookSummary = request.POST.get('book_summary')
			 		bookInfo = request.POST.get('book_info')
			 		
			 		form = Books(book_title = bookTitle, book_author = Author.objects.get(book_author_id = a.book_author_id), book_cover = bookCover, book_tags = bookTags,
			 			book_file = bookFile, book_year = bookYear, book_summary = bookSummary, book_category = Category.objects.get(book_category_no = c.book_category_no),
			 			is_bookmarked = 0, is_downloaded = 0, is_read = 0, is_deleted = 0)
			 		form.save()
			 		messages.success(request,'Book Added')
			 		return redirect('arms:addBook_view')
		else:
	 		print(form.errors)
	 		messages.warning(request,'Unsuccessful Save')
