from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	user_id = models.CharField(primary_key=True, max_length=50)
	password = models.CharField(max_length=100)
	confirmpassword = models.CharField(max_length=100 , default="")
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	birthdate = models.DateField(default = timezone.now)

	G_CHOICES = [('M','Male'),('F','Female')]
	gender=models.CharField(max_length = 50, choices=G_CHOICES)

	contact_number =  models.CharField(max_length = 15)

	class Meta:
		db_table = "User"

class Student(models.Model):
	student_id = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = "Student"

class Employee(models.Model):
	employee_id =  models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		db_table = "Employee"

class Administrator(models.Model):
	admin_id = models.CharField(primary_key=True, max_length=50)

	class Meta:
		db_table = "Administrator"

class Author(models.Model):
	book_author_id = models.CharField(primary_key=True, max_length=50)
	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	birthdate = models.DateField(default = timezone.now)
	G_CHOICES = [('M','Male'),('F','Female')]
	gender=models.CharField(max_length = 50, choices=G_CHOICES)

	class Meta:
		db_table = "Author"

class Category(models.Model):
	book_category_no = models.CharField(primary_key=True, max_length=50)
	book_category = models.CharField(max_length=100)

	class Meta:
		db_table = "Category"

class Books(models.Model):
	book_id = models.CharField(primary_key=True, max_length=50)
	book_title = models.CharField(max_length = 100)
	book_author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
	book_cover = models.ImageField(upload_to='media/')
	book_file = models.FileField(upload_to='media/')
	book_year = models.IntegerField()
	book_tags = models.CharField(max_length = 100)
	book_summary = models.CharField(max_length = 100)
	book_category_no = models.ForeignKey(Category, on_delete=models.CASCADE)
	# book_info = models.CharField(max_length = 100)
	is_bookmarked = models.BooleanField()
	is_downloaded = models.BooleanField()
	is_read = models.BooleanField()

	class Meta:
		db_table = "Books"

