from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	profile_pic = models.ImageField(upload_to='media/')

	def __str__(self):
		return self.name

class Author(models.Model):
	# book_author_id = models.CharField(primary_key=True, max_length=50)
	book_author_id = models.AutoField(primary_key=True)
	firstname = models.CharField(max_length = 100, null=True)
	lastname = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	birthdate = models.DateField(default = timezone.now)
	G_CHOICES = [('M','Male'),('F','Female')]
	gender=models.CharField(max_length = 50, choices=G_CHOICES)

	class Meta:
		db_table = "Author"

class Category(models.Model):
	# book_category_no = models.CharField(primary_key=True, max_length=50)
	book_category_no = models.AutoField(primary_key=True)
	book_category = models.CharField(max_length=100)

	class Meta:
		db_table = "Category"

class Books(models.Model):
	# book_id = models.CharField(primary_key=True, max_length=50)
	book_id = models.AutoField(primary_key=True)
	book_title = models.CharField(max_length = 100)
	book_author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
	book_cover = models.ImageField(upload_to='media/')
	book_file = models.FileField(upload_to='media/')
	book_year = models.DateField()
	book_tags = models.CharField(max_length = 100)
	book_summary = models.CharField(max_length = 100)
	book_category_no = models.ForeignKey(Category, on_delete=models.CASCADE)
	date_added = models.DateField(default=timezone.now)
	# book_info = models.CharField(max_length = 100, default="")
	is_bookmarked = models.BooleanField()
	is_downloaded = models.BooleanField()
	is_read = models.BooleanField()

	is_deleted= models.BooleanField(default=False)
	
	class Meta:
		db_table = "Books"

