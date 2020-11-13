from django.db import models

# Create your models here.

class Person(models.Model):

	firstname = models.CharField(max_length = 100)
	lastname = models.CharField(max_length = 100)

	G_CHOICES = [('M','Male'),('F','Female')]
	gender=models.CharField(max_length = 50, choices=G_CHOICES)

	class Meta:
		db_table = "Person"

class Books(models.Model):

	bookTitle = models.CharField(max_length = 100)
	bookAuthor = models.CharField(max_length = 100)
	bookCover = models.FileField(upload_to='media')
	yearPublished = models.IntegerField()
	bookTags = models.CharField(max_length = 100)
	bookSummary = models.CharField(max_length = 100)
	bookCategory = models.CharField(max_length = 100)

	class Meta:
		db_table = "Books"

class User(Person):
	userID = models.IntegerField()
	password = models.CharField(max_length = 100)
	books = models.ManyToManyField(Books)

	class Meta:
		db_table = "User"

class Administrator(Person):
	userID = models.IntegerField()
	password = models.CharField(max_length = 100)
	books = models.ManyToManyField(Books)

	class Meta:
		db_table = "Administrator"

