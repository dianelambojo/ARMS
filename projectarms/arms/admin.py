from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Category)