from django.core.checks.messages import Info
from django.shortcuts import redirect, render
from django.utils.html import DOTS
from . import backgroundLogic
from .models import Course,Teacher,OddSem,EvenSem
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CourseForm, TeacherEditForm, TeacherForm, CourseEditForm


def home(request):
	
	return render(request,'courseDist/home.html')


def odd(request):
	
	courses = Course.objects.all()
	teachers = Teacher.objects.all()
	tl = [t for t in teachers if t.isActive]
	cl = [c for c in courses if c.semester==1]
	if request.method == 'POST':
		C = []
		opt = request.POST
		for c in cl:
			if c.semester == 1:
				if c.isoptional:
					if c.code in opt:
						C.append(c)
				else:
					C.append(c)

		if 'jun_to_sen' in opt:
			dist = backgroundLogic.assign(tl,C,True)
		elif 'sen_to_jun' in opt:
			dist = backgroundLogic.assign(tl,C,False)
		

		context = {
			'frst' : dist.get(1),
			'scnd' : dist.get(2),
			'thrd' : dist.get(3),
			'frth' : dist.get(4),
			'teachers' : tl,
			'sem' : 'First'
		}

		OddSem.objects.all().delete()

		for _ in context['frst']:
			OddSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=1)
		for _ in context['scnd']:
			OddSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=2)
		for _ in context['thrd']:
			OddSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=3)
		for _ in context['frth']:
			OddSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=4)

		return render(request,'courseDist/dist.html',context)

	def f(c):
		return 10*c.year+c.semester
	cl.sort(key=f)
	context = {
		'courses' : cl
	}
	return render(request,'courseDist/odd.html',context)

def even(request):
	
	courses = Course.objects.all()
	teachers = Teacher.objects.all()
	tl = [t for t in teachers if t.isActive]
	cl = [c for c in courses if c.semester==2]
	if request.method == 'POST':
		C = []
		opt = request.POST
		for c in cl:
			if c.semester == 2:
				if c.isoptional:
					if c.code in opt:
						C.append(c)
				else:
					C.append(c)

		if 'jun_to_sen' in opt:
			dist = backgroundLogic.assign(tl,C,True)
		elif 'sen_to_jun' in opt:
			dist = backgroundLogic.assign(tl,C,False)

		context = {
			'frst' : dist.get(1),
			'scnd' : dist.get(2),
			'thrd' : dist.get(3),
			'frth' : dist.get(4),
			'teachers' : tl,
			'sem' : 'Second'
		}

		EvenSem.objects.all().delete()

		for _ in context['frst']:
			EvenSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=1)
		for _ in context['scnd']:
			EvenSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=2)
		for _ in context['thrd']:
			EvenSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=3)
		for _ in context['frth']:
			EvenSem.objects.create(title=_[1],code=_[0],credit_hour=_[2],frstSetter=_[3],year=4)

		return render(request,'courseDist/dist.html',context)

	def f(c):
		return 10*c.year+c.semester
	cl.sort(key=f)
	context = {
		'courses' : cl
	}
	return render(request,'courseDist/even.html',context)


def oddsem(request):

	records = OddSem.objects.all()
	
	courses = {1:[],
		   2:[],
	   	   3:[],
		   4:[]
	}

	for record in records:
		courses[record.year].append(record)

	context = {
			'frst' : courses.get(1),
			'scnd' : courses.get(2),
			'thrd' : courses.get(3),
			'frth' : courses.get(4),
			'sem' : 'First'
		}

	return render(request,'courseDist/oddsem.html',context)

def evensem(request):

	records = EvenSem.objects.all()
	
	courses = {1:[],
		   2:[],
	   	   3:[],
		   4:[]
	}

	for record in records:
		courses[record.year].append(record)

	context = {
			'frst' : courses.get(1),
			'scnd' : courses.get(2),
			'thrd' : courses.get(3),
			'frth' : courses.get(4),
			'sem' : 'Second'
		}

	return render(request,'courseDist/evensem.html',context)

def allcourses(request):
	
	courses = Course.objects.all()
	cl = [c for c in courses]
	def f(c):
		return 10*c.year+c.semester
	cl.sort(key=f)
	context = {
		'courses' : cl
	}
	return render(request,'courseDist/allcourses.html',context)

def allteachers(request):
	
	teachers = Teacher.objects.all()
	tl = [t for t in teachers]
	def f(t):
		return t.seniority
	tl.sort(key=f)
	context = {
		'teachers' : tl
	}
	return render(request,'courseDist/allteachers.html',context)

def distro1(request):
	
	courses = OddSem.objects.all()

	cl = [c for c in courses]

	d = request.POST
	for c in cl:
		if not d.get(c.code) == None:
			crs = OddSem.objects.get(code=c.code)
			crs.scndSetter = d.get(c.code)
			crs.save()

	messages.success(request,f'Courses Have Been Assigned Successfully.')
	return redirect('oddsem')



def distro2(request):
	
	courses = EvenSem.objects.all()

	cl = [c for c in courses]

	d = request.POST
	for c in cl:
		if not d.get(c.code) == None:
			crs = EvenSem.objects.get(code=c.code)
			crs.scndSetter = d.get(c.code)
			crs.save()

	messages.success(request,f'Courses Have Been Assigned Successfully.')
	return redirect('evensem')


def register(request):
	
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'Account created for {username} !')
			return redirect('home')
	else:
		form = UserCreationForm()
	return render(request,'courseDist/register.html',{'form': form})

def addcourse(request):

	if request.method == 'POST':
		form = CourseForm(request.POST)
		if form.is_valid():
			form.save()
			title = form.cleaned_data.get('title')
			messages.success(request,f'{title} Has been added Successfully!')
			return redirect('allcourses')
	else:
		form = CourseForm()
	return render(request,'courseDist/addcourse.html',{'form': form})

def editcourse(request):

	if request.method == 'POST':
	
		form = CourseEditForm(request.POST)
		c = request.POST.get('code')
		title = request.POST.get('title')
		credit_hour = request.POST.get('credit_hour')
		isoptional = request.POST.get('isoptional')
		year = request.POST.get('year')
		semester = request.POST.get('semester')
		crs = Course.objects.get(code=c)
		if not title == None:
			crs.title = title
		if not credit_hour == None:
			crs.credit_hour = credit_hour
		if not isoptional == None:
			crs.isoptional = True
		else:
			crs.isoptional = False
		if not year == None:
			crs.year = year
		if not semester == None:
			crs.semester = semester
		crs.save()
		messages.success(request,f'{title} Has been edited Successfully!')
		return redirect('allcourses')
	else:
		form = CourseEditForm()
	return render(request,'courseDist/editcourse.html',{'form': form})

def addteacher(request):

	if request.method == 'POST':
		form = TeacherForm(request.POST)
		if form.is_valid():
			form.save()
			name = form.cleaned_data.get('name')
			messages.success(request,f'{name} Has Joined Successfully!')
			return redirect('allteachers')
	else:
		form = TeacherForm()
	return render(request,'courseDist/addteacher.html',{'form': form})

def editteacher(request):

	if request.method == 'POST':
	
		form = TeacherEditForm(request.POST)
		c = request.POST.get('code_name')
		name = request.POST.get('name')
		isActive = request.POST.get('isActive')
		email = request.POST.get('email')

		tchr = Teacher.objects.get(code_name=c)
		if not name == None:
			tchr.name = name
		if not isActive == None:
			tchr.isActive = True
		else:
			tchr.isActive = False
		if not email == None:
			tchr.email = email

		tchr.save()
		messages.success(request,f'Info of {name} has been edited Successfully!')
		return redirect('allteachers')
	else:
		form = TeacherEditForm()
	return render(request,'courseDist/editteacher.html',{'form': form})