from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

#paths arranged alphabetically by name
app_name = 'arms'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('dashboard', views.ArmsAdminView.as_view(), name="arms_admin_view")
    path('homepage', views.HomepageView.as_view(), name="homepage_view")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)