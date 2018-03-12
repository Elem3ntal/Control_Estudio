from django.contrib import admin
from control_academico.apps.gestionCursos.models import *

# Register your models here.

class AdminPersonal(admin.ModelAdmin):
    list_display = ["dni", "surnames", "names", "sex", "personaltype"]
    list_filter = ["personaltype"]
    #list_display_links = ["surnames"]
    #list_editable = ["names"]
    search_fields = ["dni"]
    class Meta:
        model = Personal


class AdminCourse(admin.ModelAdmin):
    list_display = ["code", "name", "uc", "status"]
    list_filter = ["name"]
    search_fields = ["code","status"]
    class Meta:
        model = Course


class AdminEnrollment(admin.ModelAdmin):
    list_display = ["id_course", "id_student", "date_enrollment"]
    list_filter = ["id_course"]
    search_fields = ["id_course"]
    class Meta:
        model = Enrollment
        

class AdminTest(admin.ModelAdmin):
    list_display = ["id_enrollment", "ptos"]
    list_filter = ["id_enrollment"]
    #search_fields = ["id_course"]
    class Meta:
        model = Test


admin.site.register(Personal, AdminPersonal) 
admin.site.register(Course, AdminCourse)
admin.site.register(Enrollment, AdminEnrollment)
admin.site.register(Test, AdminTest) 
