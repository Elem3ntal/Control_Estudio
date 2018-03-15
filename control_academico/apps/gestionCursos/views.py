import json
from django.shortcuts import render
from control_academico.apps.gestionCursos.models import *
from django.utils import timezone
from django.db.models import Avg, Max, Min, Count
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

def index(request):
	alumno = Test.objects.all().values('id_enrollment__id_student__surnames' ,'id_enrollment__id_student__names').annotate(dcount=Avg('ptos'))
	context = {
    	"alumnos" : alumno,
	}
	return render(request, "index.html", context)


def reprobados(request):
	alumno = Test.objects.all().values('id_enrollment__id_student__surnames' ,'id_enrollment__id_student__names').annotate(dcount=Avg('ptos')).exclude(dcount__gte=10)
	context = {
    	"alumnos" : alumno,
	}
	return render(request, "index.html", context)

def aprobados(request):
	alumno = Test.objects.all().values('id_enrollment__id_student__surnames' ,'id_enrollment__id_student__names').annotate(dcount=Avg('ptos')).filter(dcount__gte=10)
	context = {
    	"alumnos" : alumno,
	}
	return render(request, "index.html", context)

def agenda(request):
	return render(request, "agenda.html", {})

def calendar(request):
	data = json.load(open("C:\\Users\\Martin\\Desktop\\Destacame\\control_academico\\static\\js\calendar.json"))
	return JsonResponse(data)

class CourseList(ListView):
    model = Course

class CourseDetail(DetailView):
    model = Course

class CourseCreation(CreateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name','uc','code','status']

class CourseUpdate(UpdateView):
    model = Course
    success_url = reverse_lazy('courses:list')
    fields = ['name','uc','code','status']


class CourseDelete(DeleteView):
    model = Course
    success_url = reverse_lazy('courses:list')

	