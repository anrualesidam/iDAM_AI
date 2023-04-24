from django import forms
from django.contrib.auth.forms import UserCreationForm

class ArchivoForm(forms.Form):
    archivo = forms.FileField()


class MyUserCreationForm(UserCreationForm):
    username = forms.RegexField(label=("Correo"), max_length=30, regex=r'^[\w.@+-]+$',
       help_text = ("Requerido. 30 carácteres como máximo. Únicamente letras, dígitos y @/./+/-/_"),
        error_messages = {'invalid': ("Esta casilla debe contener únicamente letras, dígitos y @/./+/-/_")})

class ContactForm(forms.Form): 
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)