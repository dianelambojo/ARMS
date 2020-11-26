from django import forms
from .models import *

class UserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('password','firstname')

class StudentForm(forms.ModelForm):

	class Meta:
		model = Student
		fields = ('student_id',)

class EmployeeForm(forms.ModelForm):

	class Meta:
		model = Employee
		fields = ('employee_id',)

class BooksForm(forms.ModelForm):

	class Meta:
		model = Books
		fields=('book_id',)