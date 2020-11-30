from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from arms.models import Books, Author

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

class AuthorForm(forms.ModelForm):

 	class Meta:
 		model = Author
 		fields=('book_author_id',)

class BooksForm(forms.ModelForm):

 	class Meta:
 		model = Books
 		fields=('book_id',)

