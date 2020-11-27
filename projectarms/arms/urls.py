from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#paths arranged alphabetically by name
app_name = 'arms'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('dashboard', views.ArmsAdminView.as_view(), name="arms_admin_view"),
    path('homepage', views.HomepageView.as_view(), name="homepage_view"),
    path('profile', views.ProfileIndexView.as_view(), name='profile_view'),
    path('landingpage', views.LandingPageIndexView.as_view(), name='landingpage_view'),
    path('register/', views.RegisterIndexView.as_view(), name='register_view'),
    path('login', views.LoginIndexView.as_view(), name='login_view'),
    path('aboutUs', views.AboutUsIndexView.as_view(), name='aboutUs_view'),
    path('addbook', views.AddBookIndexView.as_view(), name='addBook_view'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)