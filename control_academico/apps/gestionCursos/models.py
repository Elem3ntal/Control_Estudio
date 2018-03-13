from django.db import models
from django.db.models import Q

# Create your models here.

class Personal(models.Model): 
    sexes = (('F','Femenino'),('M','Masculino'))
    personal_type = (('P','Profesor'),('A','Alumno'))

    surnames = models.CharField(max_length=35)
    names = models.CharField(max_length=35)
    dni = models.CharField(max_length=35)
    birthdate = models.DateField(max_length=35)
    sex = models.CharField(max_length=1, choices=sexes, default='M')
    personaltype = models.CharField(max_length=1, choices=personal_type, default='A')

    def PersonalInformation(self):
        strings = "{0} {1}"
        return strings.format(self.surnames, self.names)

    def __str__(self):
        return self.PersonalInformation()

    def Type(self):
        return self.personaltype == 'P'

    teachertype = property(Type) 


def limitoptions(v):
    # De esta forma puedo filtrar los elementos por su atributo property
    list_pks = [obj.pk for obj in Personal.objects.all() if obj.teachertype == v] 
    return Q(pk__in = list_pks)


class Course(models.Model):
    name = models.CharField(max_length=50)
    uc = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=35)
    status = models.BooleanField(default=True)
    id_teachers = models.ForeignKey(Personal, models.DO_NOTHING, db_column='Id_teachers', limit_choices_to = limitoptions(True)) 
    
    def __str__(self):
        return "{0}".format(self.name)


class Enrollment(models.Model):
    id_student = models.ForeignKey(Personal, models.DO_NOTHING, db_column='Id_student', limit_choices_to = limitoptions(False))
    id_course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    date_enrollment = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        strings = "{0} => {1}"
        return strings.format(self.id_student, self.id_course.name)

        
class Test(models.Model):
    id_enrollment = models.ForeignKey(Enrollment, null=False, blank=False, on_delete=models.CASCADE)
    ptos = models.PositiveSmallIntegerField()

    def __str__(self):
        strings = "{0}, {1}"
        return strings.format(self.id_enrollment, self.ptos)

