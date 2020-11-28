from django.shortcuts import render,redirect
from django.views.generic import View
from django.http import HttpResponse
from django.http import Http404
from .forms import *
from .models import *
import re


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

class LoginIndexView(View):
	def get(self, request):
		return render(request, 'login.html')

class RegisterIndexView(View):
	def get(self,request):
		context={
			'title': 'Registration'
		}
		return render(request, 'register.html', context)

	def post(self, request):
		form = UserForm(request.POST)
		if form.is_valid():
			
			user_id = request.POST.get("user_id")
			firstname = request.POST.get("firstname")
			lastname = request.POST.get("lastname")
			birthdate = request.POST.get("birthdate")
			email = request.POST.get("email")
			gender = request.POST.get("gender")
			contact_number = request.POST.get("contact_number")
			password = request.POST.get("password")
			confirmpassword = request.POST.get("confirmpassword")
			# user_type = request.POST.get("user_type")

			pattern_student = r'[0-9]{2}-[0-9]{4}-[0-9]{3}'
			patter_emp = r'^[0-9]*$'

			if re.findall(pattern_student,string=user_id):
				form = User(user_id = user_id, firstname = firstname, lastname = lastname, birthdate = birthdate, email=email, gender = gender, contact_number = contact_number,
						password = password, confirmpassword = confirmpassword)

				form.save()

				form = StudentForm(request.POST)

				form = Student(student_id = User.objects.get(user_id = user_id))

				form.save()

				return HttpResponse('Record saved!')

			elif re.findall(patter_emp,string=user_id):
				form = User(user_id = user_id, firstname = firstname, lastname = lastname, birthdate = birthdate, email=email, gender = gender, contact_number = contact_number,
						password = password, confirmpassword = confirmpassword)

				form.save()

				form = EmployeeForm(request.POST)

				form = Employee(employee_id = User.objects.get(user_id = user_id))

				form.save()

				return HttpResponse('Record saved!')

			else:
				return HttpResponse('wrong pattern')
			
		else: 
			print(form.errors)	
			return HttpResponse('Not saved!')

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

	def post(self, request):
		form = BooksForm(request.POST, request.FILES)
		if form.is_valid():
			book_id = request.POST.get('book_id')
			book_title = request.POST.get('book_title')
			book_author_id = request.POST.get('book_author_id')
			book_cover = request.FILES['book_cover']
			book_file = request.FILES['book_file']
			book_year = request.POST.get('book_year')
			book_tags = request.POST.get('book_tags')
			book_summary = request.POST.get('book_summary')
			book_category_no = request.POST.get('book_category_no')
			book_info = request.POST.get('book_info')
			form = Books(book_id = book_id, book_title = book_title, book_author_id = book_author_id, book_cover = book_cover,
				book_file = book_file, book_year = book_year, book_tags = book_tags, book_summary = book_summary, book_category_no = book_category_no, book_info = book_info)
			form.save()
			return HttpResponse('Book Saved!')
		else:
			print(form.errors)
			return HttpResponse('Not Valid')