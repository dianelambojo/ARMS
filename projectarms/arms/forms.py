from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from arms.models import Books, Author, Category

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class AuthorForm(forms.ModelForm):

 	class Meta:
 		model = Author
 		fields=('firstname','lastname','birthdate','email')

class BooksForm(forms.ModelForm):

 	class Meta:
 		model = Books
 		fields = ('book_title','book_author','book_cover','book_file','book_year','book_tags','book_summary','book_category',)
 		# fields = '__all__'

class CategoryForm(forms.ModelForm):

 	class Meta:
 		model = Category
 		fields=('book_category',)