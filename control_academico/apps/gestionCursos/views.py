from django.shortcuts import render
from control_academico.apps.gestionCursos.models import *
from django.utils import timezone
from django.db.models import Avg, Max, Min, Count

# Create your views here.
def index(request):
	alumno = Test.objects.all().values('id_enrollment__id_student__surnames' ,'id_enrollment__id_student__names').annotate(dcount=Avg('ptos'))
	#Test.objects.all().values('id_enrollment__id_student__surnames' ,'id_enrollment__id_student__names').annotate(dcount=Avg('ptos')).filter(dcount__gte=10)
	context = {
    	"alumnos" : alumno,
	}
	return render(request, "index.html", context)

def agenda(request):
	return render(request, "agenda.html", {})
    

	
	