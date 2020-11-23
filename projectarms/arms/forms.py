from django import forms
from .models import *

class UserForm(forms.ModelForm):
<<<<<<< HEAD
    user_id = forms.CharField(required=False)
    password = forms.CharField(required=False)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.CharField(required=False)
    birthdate = forms.DateField(required=False) 
    contact_number =  forms.CharField(required=False) 

    class Meta:
        model = User
        fields =  ('user_id' ,'password','firstname', 'lastname', 'email',
        'birthdate','contact_number')
=======

	class Meta:
		model = User
		fields = ('password','firstname')
>>>>>>> c728571666b461a9641b91f0a6a8b2da7d3f106e
