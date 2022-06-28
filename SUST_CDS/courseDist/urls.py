from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('odd/',views.odd,name="odd"),
    path('even/',views.even,name="even"),
    path('dist1/',views.distro1,name="distro1"),
    path('dist2/',views.distro2,name="distro2"),
    path('allcourses/',views.allcourses,name="allcourses"),
    path('allteachers/',views.allteachers,name="allteachers"),
    path('register/',views.register,name="register"),
    path('addcourse/',views.addcourse,name="addcourse"),
    path('addteacher/',views.addteacher,name="addteacher"),
    path('editcourse/',views.editcourse,name="editcourse"),
    path('editteacher/',views.editteacher,name="editteacher"),
    path('oddsem/',views.oddsem,name="oddsem"),
    path('evensem/',views.evensem,name="evensem")
]