from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from .forms import MyUserCreationForm

# Create your views here.


def Home(request):
        return render(request,"base.html")

def QuienesSomos(request):
        return render(request,"quienesomos.html")

def Contactanos(request):
        return render(request,"contactanos.html")

@csrf_protect
def SignIn(request):
    #verification of email and password given. this process was found on Django documentation
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/Welcome/')  #redirection to new page if login is successful
        else:
            messages.success(request, "There was an error loggin in, try again") #Error message to display
            return render(request, 'SignIn.html', {})                #Reload of the page to attempt a new login

    else:
        return render(request, 'SignIn.html', {})                    #First page to show at arrival

@csrf_protect
def Register(request):
        if request.method == "POST":
                form = MyUserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password1')
                        user = authenticate(username=username, password=password)
                        if user is not None:

                                subject = 'Registro Exitoso'
                                email_template_name = 'register_email.txt'
                                c = {
                                'protocol': 'http',
                                'domain': '127.0.0.1:8000'
                                }
                                email = render_to_string(email_template_name, c)
                                try:
                                        send_mail(subject, email, 'admin@idam.com', [username], fail_silently=False)
                                except BadHeaderError:
                                        return HttpResponse('Invalid header found.')

                                login(request, user)
                                return redirect('/Welcome/')
                        else:
                                messages.success(request, "Hubo un error en tu registro")
                                return render(request, 'Register.html',{'form':form,})
                else:
                        messages.success(request, "Hubo un error en tu registro")
                        return render(request, 'Register.html',{'form':form,})
        else:
                form = MyUserCreationForm()
                return render(request, 'Register.html',{'form':form,})

def AnaliticaAvanzada(request):
        return render(request,"AnaliticaAvanzada.html")

def IngenieroDatos(request):
        return render(request,"IngenieroDatos.html")

def FormacionCapacitacion(request):
        return render(request,"FormacionCapacitacion.html")

def LaboratorioData(request):
        return render(request,"LaboratorioData.html")

