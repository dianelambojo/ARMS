from django import forms
from .models import *

class UserForm(forms.ModelForm):
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