from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields.related import ForeignKey

class Course(models.Model):

	title = models.CharField(max_length=100)
	code = models.CharField(max_length=10,primary_key=True)
	credit_hour = models.DecimalField(decimal_places=2,max_digits=3)
	ispaid = models.BooleanField()
	isoptional = models.BooleanField()
	year = models.PositiveIntegerField(default=1)
	semester = models.PositiveIntegerField(default=1)
	isSessional = models.BooleanField(default=False)
	isOffered = models.BooleanField(default=True)

	def __str__(self) -> str:
	    return self.title

class Teacher(models.Model):

	name = models.CharField(max_length=100)
	code_name = models.CharField(max_length=10,primary_key=True)
	seniority = models.PositiveIntegerField() # Most Senior teacher has the least seniority number and vice-versa.
	email = models.EmailField(default=" ")
	isActive = models.BooleanField(default=True)

	def __str__(self) -> str:
	    return self.code_name

class OddSem(models.Model):

	title = models.CharField(max_length=100)
	code = models.CharField(max_length=10,primary_key=True)
	credit_hour = models.DecimalField(decimal_places=2,max_digits=3)
	ispaid = models.BooleanField(default=False)
	isoptional = models.BooleanField(default=False)
	year = models.PositiveIntegerField(default=1)
	semester = models.PositiveIntegerField(default=1)
	isSessional = models.BooleanField(default=False)
	isOffered = models.BooleanField(default=True)
	frstSetter = models.CharField(max_length=100)
	scndSetter = models.CharField(max_length=100,null=True)

	def __str__(self) -> str:
	    return self.code

class EvenSem(models.Model):

	title = models.CharField(max_length=100)
	code = models.CharField(max_length=10,primary_key=True)
	credit_hour = models.DecimalField(decimal_places=2,max_digits=3)
	ispaid = models.BooleanField(default=False)
	isoptional = models.BooleanField(default=False)
	year = models.PositiveIntegerField(default=1)
	semester = models.PositiveIntegerField(default=1)
	isSessional = models.BooleanField(default=False)
	isOffered = models.BooleanField(default=True)
	frstSetter = models.CharField(max_length=100)
	scndSetter = models.CharField(max_length=100,null=True)

	def __str__(self) -> str:
	    return self.code