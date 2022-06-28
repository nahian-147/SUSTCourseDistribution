from django import forms
from .models import Course,Teacher

class CourseForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['title',
			  'code',
			  'credit_hour',
			  'ispaid',
			  'isoptional',
			  'year',
			  'semester',
			  'isSessional'
		]

class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['name',
			  'code_name',
			  'seniority',
			  'email',
		]

class CourseEditForm(forms.ModelForm):
	class Meta:
		model = Course
		fields = ['code',
			  'title',
			  'credit_hour',
			  'isoptional',
			  'year',
			  'semester'
		]

class TeacherEditForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['code_name',
			  'name',
			  'isActive',
			  'email',
		]