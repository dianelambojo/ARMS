from django.urls import path
from . import views

app_name = 'arms'
urlpatterns = [

    path('homepage', views.HomepageView.as_view(), name="homepage_view")
    
]