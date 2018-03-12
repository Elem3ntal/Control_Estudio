from django import forms

class RegistrarForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()