from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from control_academico.apps.gestionCursos import views

from control_academico.apps.gestionCursos.views import (
    CourseList,
    CourseDetail,
    CourseCreation,
    CourseUpdate,
    CourseDelete
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path('reprobados/', views.reprobados, name='reprobados'),
    path('aprobados/', views.aprobados, name='aprobados'),
    url(r'^cursos/$', CourseList.as_view(), name='list'),
    url(r'^cursos/(?P<pk>\d+)$', CourseDetail.as_view(), name='detail'),
    url(r'^cursos/nuevo$', CourseCreation.as_view(), name='new'),
    url(r'^cursos/editar/(?P<pk>\d+)$', CourseUpdate.as_view(), name='edit'),
    url(r'^cursos/borrar/(?P<pk>\d+)$', CourseDelete.as_view(), name='delete'),
    url(r'^api/calendar/$', views.calendar, name='calendar'),
    
]
