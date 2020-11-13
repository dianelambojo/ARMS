from django.urls import path
from . import views

app_name = 'Profile'
urlpatterns = [
    path('Profile', views.ProfileIndexView.as_view(), name='Profile_view'),
]