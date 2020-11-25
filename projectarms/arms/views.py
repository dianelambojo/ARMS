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
		return render(request, 'addbook.html')
		