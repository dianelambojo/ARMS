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
import datetime
from django.core.paginator import Paginator, EmptyPage

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
				# if the user tries to search using the authors first or last name
				# if the author is found then it will proceed to search for the book that was written by the author
				# allBook = Books.objects.all()
				authors = Author.objects.filter(Q(firstname__icontains=search) | Q(lastname__icontains=search))
				for author in authors:
					# for a in allBook:
					# 	if author.book_author_id == a.book_author_id_id:
					books = Books.objects.filter(book_author_id=author.book_author_id)

					p = Paginator(books,20)
					page_num = request.GET.get('page', 1)
					try:
						page = p.page(page_num)
					except:
						page = p.page(1)

					context={
						'search' : search,
						'books' : page,
						'authors' : authors,
					}
					return render(request, 'results.html', context)
						# else:
						# 	context = {
						# 		'search' : search
						# 	}
						# 	return render(request, 'results.html', context)
						
				# if the user tries to search using the book title or year 
				books = Books.objects.filter(Q(book_title__icontains=search) | Q(book_year__icontains=search))
				authors = authors = Author.objects.all()
				context={
					'search' : search,
					'books' : books,
					'authors' : authors,
				}

				return render(request, 'results.html', context)

			#By category searched of all books
			searched = request.GET.get('searched')
			if searched == 'research':
				authors = authors = Author.objects.all()
				books = Books.objects.all()
				research = Category.objects.filter(Q(book_category = searched))
				for r in research:
					books = Books.objects.filter(book_category_no_id=r.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Research Studies',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Research Studies'})	
			if searched == 'journals':
				authors = authors = Author.objects.all()
				books = Books.objects.all()
				journals = Category.objects.filter(Q(book_category = searched))
				for j in journals:
					books = Books.objects.filter(book_category_no_id=j.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Journals',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Journals'})	
			if searched == 'filipiniana':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Filipiniana',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Filipiniana'})	
			if searched == 'engineering':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Engineering',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Engineering'})	
			if searched == 'computerscience':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Computer Science',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Computer Science'})	
			if searched == 'informationtechnology':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Information Technology',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Information Technology'})	
			if searched == 'business':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Business',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Business'})	
			if searched == 'architecture':
				books = Books.objects.all()
				authors = authors = Author.objects.all()
				filipiniana = Category.objects.filter(Q(book_category = searched))
				for f in filipiniana:
					books = Books.objects.filter(book_category_no_id=f.book_category_no)
					context={
						'authors' : authors,
						'books' : books,
						'search' : 'Architecture',
					}
					return render(request, 'results.html', context)

				return render(request, 'results.html', {'search' : 'Architecture'})	
			#if not search/searched
			else: 	
				# new releases within the month of the year (more or less)
				today = datetime.date.today()
				books = Books.objects.filter(date_added__year=today.year, date_added__month=today.month)
				print(books)
				authors = Author.objects.all()
				context={
					'books' : books,
					'authors' : authors,
				}
				return render(request, 'homepage.html', context)
		#if request.method != GET else
		else:
			# today = datetime.date.today()
			# books = Books.objects.filter(date_added__year=today.year, date_added__month=today.month)
			# print(books)
			# authors = Author.objects.all()
			# context={
			# 	'books' : books,
			# 	'authors' : authors,
			# }
			return render(request, 'homepage.html')			

class ProfileIndexView(View):
	def get(self, request):
		user = User.objects.all()
		books = Books.objects.all()
		authors = Author.objects.all()
		#print(user)
		context = {
			'users' : user,
			'books' : books,
			'authors' : authors,
			
		}

		return render(request, 'profile.html', context)

	def post(self, request):
		if request.method == 'POST':
			if 'btnUpdate' in request.POST:
				print('update profile button clicked')
				sid = request.POST.get("user-id")
				username = request.POST.get("username")			
				first_name = request.POST.get("firstname")
				last_name = request.POST.get("lastname")
				email = request.POST.get("email")
				
				update_user = User.objects.filter(id = sid).update(username=username,first_name=first_name,last_name=last_name,email=email)
				
				print(update_user)
				print('profile updated')

			elif 'btnDelete' in request.POST:	
				print('delete button clicked')
				sid = request.POST.get("book-id")
				book = Books.objects.filter(book_id = sid).delete()
				author = Author.objects.filter(book_author_id = sid).delete()
				print('record deleted')

		return render(request, 'profile.html')

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