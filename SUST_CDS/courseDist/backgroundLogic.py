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

	def __init__(self,title,code,credit_hour):
		self.title,self.code,self.credit_hour = title,code,credit_hour
		if(len(self.code) > 6):
			self.ispaid = True
	
	def print_course_info(self):
		print(self.title,self.code,self.credit_hour,self.ispaid,self.isoptional,self.assignedTeachers)


class Optional(Course):
	def __init__(self, title, code, credit_hour):
	    super().__init__(title, code, credit_hour)
	    self.isoptional = True

def assign(teachers,courses,rvrs):
	
	d = dict()

	for crs in courses:
		if not crs.isSessional:
			lab = crs.code.replace(crs.code[3:6],str(int(crs.code[3:6])+1))
			for l in courses:
				if l.code == lab:
					d[crs.code] = l
					courses.remove(l)

	def ft(k):
		return k.seniority

	def fc(k):
		return k.ispaid or k.isoptional

	teachers.sort(key=ft,reverse=rvrs)
	courses.sort(key=fc,reverse=True)
	
	dist = {1:[],
		2:[],
		3:[],
		4:[]
	}

	k = 0
	l = len(teachers)
	
	for course in courses:
		dist[course.year].append([course.code,course.title,course.credit_hour,teachers[k%l].name])
		if course.code in d:
			crs = d[course.code]
			dist[course.year].append([crs.code,crs.title,crs.credit_hour,teachers[k%l].name])
		k += 1 
	
	return dist
