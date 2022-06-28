from django.contrib import admin
from .models import Course,Teacher,EvenSem,OddSem

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(OddSem)
admin.site.register(EvenSem)