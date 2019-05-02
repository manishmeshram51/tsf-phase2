from django.db import models

# Create your models here.

class employee(models.Model):
	eid = phone = models.CharField(max_length=10)
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	phone = models.CharField(max_length=40)
	username = models.CharField(max_length=40)
	
	def __str__(self):
		return self.firstname
		
class student(models.Model):
	sid = phone = models.CharField(max_length=10)
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	phone = models.CharField(max_length=40)
	username = models.CharField(max_length=40)
	classs = models.CharField(max_length=40)
	
	def __str__(self):
		return self.firstname		

		
class teacher(models.Model):
	tid = phone = models.CharField(max_length=10)
	firstname = models.CharField(max_length=40)
	lastname = models.CharField(max_length=40)
	email = models.CharField(max_length=40)
	phone = models.CharField(max_length=40)
	username = models.CharField(max_length=40)
	subject = models.CharField(max_length=40)

	def __str__(self):
		return self.firstname		

