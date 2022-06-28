class Teacher:

	name = ""
	code_name = ""
	seniority = 0 # Most Senior teacher has the least seniority number and vice-versa.
	email = ""

	def __init__(self,name,code_name,seniority):
		self.name,self.code_name,self.seniority = name,code_name, seniority

	def print_teacher_info(self):
		print(self.name,self.code_name,self.seniority)
		print(self.assigned_courses)
		

class Course:
	title = ""
	code = ""
	credit_hour = 0.0
	ispaid = False 
	isoptional = False
	year = 1
	semester = 1

	def __init__(self,title,code,credit_hour,year):
		self.title,self.code,self.credit_hour,self.year = title,code,credit_hour,year
		if(len(self.code) > 6):
			self.ispaid = True
	
	def print_course_info(self):
		print(self.title,self.code,self.credit_hour,self.ispaid,self.isoptional,self.assignedTeachers)


class Optional(Course):
	def __init__(self, title, code, credit_hour,year):
	    super().__init__(title, code, credit_hour,year)
	    self.isoptional = True


t0 = Teacher('t0','TZ',4)
t1 = Teacher('t1','TO',1)
t2 = Teacher('t2','TT',0)
t3 = Teacher('t3','TH',3)
t4 = Teacher('t4','TF',2)

c0 = Course("Theory of Computation",'CSE235',3.0,2)
c1 = Course("DataBase Systems",'CSE333',3.0,3)
c2 = Course("Operating System",'CSE331',3.0,3)
c3 = Course("Compiler Construction",'CSE439',3.0,2)
c4 = Course("Intro to Programming",'CSE209D',3.0,1)
c5 = Course("Intro to CSE",'CSE203D',3.0,1)
c6 = Optional("Bioinformatics",'CSE459',3.0,4)
c7 = Optional("Machine Learning",'CSE435',3.0,4)
c8 = Course("Artificial Intelligence",'CSE401',3.0,4)
c9 = Course("Data Structure & Algorithms",'CSE133',3.0,1)
c10 = Optional("Intro to Cyber Security",'CSE477',3.0,4)

teachers = [t0,t1,t2,t3,t4]
courses = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

def assign(teachers,courses):
	def ft(k):
		return k.seniority

	def fc(k):
		return k.ispaid or k.isoptional

	teachers.sort(key=ft,reverse=True)
	courses.sort(key=fc,reverse=True)
	
	dist = dict()

	k = 0
	l = len(teachers)
	
	for course in courses:
		dist[course.code] = [course.title,course.credit_hour,teachers[k%l].code_name,course.year]
		k += 1 
		
	
	
	frst = [(code,dist[code]) for code in dist if dist[code][3]==1]
	scnd = [(code,dist[code]) for code in dist if dist[code][3]==2]
	thrd = [(code,dist[code]) for code in dist if dist[code][3]==3]
	frth = [(code,dist[code]) for code in dist if dist[code][3]==4]

	return (frst,scnd,thrd,frth)
	


print(assign(teachers,courses))
