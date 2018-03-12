from django.shortcuts import render
from control_academico.apps.gestionCursos.models import *
from django.utils import timezone
#from control_academico.apps.gestionCursos.models import *
#from .forms import RegistrarForm

# Create your views here.
def index(request):
	alumno = Test.objects.all()
	#Test.objects.filter(ptos=15)
	context = {
    	"alumnos" : alumno,
	}
	return render(request, "index.html", context)  

    