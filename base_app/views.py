from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from .forms import MyUserCreationForm
from .forms import ContactForm
# Create your views here.


def Home(request):
        return render(request,"base.html")

def QuienesSomos(request):
        return render(request,"quienesomos.html")

def Contactanos(request):
        if request.method == 'POST':
                #form = ContactForm(request.POST)

                name = request.POST['name']
                email = request.POST['email'] 
                subject = request.POST['subject']
                message = request.POST['message']

                template = render_to_string('email_template.html', {
                        'name': name, 
                        'email': email, 
                        'message': message
                })

                email = EmailMessage(
                        subject,
                        template, 
                        settings.EMAIL_HOST_USER,
                        ['admin@idam.com'] # aca llega el correo
                )

                email.fail_silently = False # no marque error en gmail 
                email.send()

                messages.success(request, 'Se ha enviado tu correo.')

                return redirect('contactanos')
        
        else:
                form = ContactForm()
                


        return render(request, "contactanos.html", {
                'form': form
        })

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
                                'protocol': 'https',
                                'domain': 'idamm.com.co',
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

@csrf_protect
def password_reset_request(request):
        if request.method == 'POST':
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                      #  password_reset_form.save()
                        data = password_reset_form.cleaned_data.get('email')
                        associated_users = User.objects.filter(Q(username=data))
                        if associated_users.exists():
                                for user in associated_users:
                                        subject = 'Reestablecimiento de contraseña solicitado'
                                        email_template_name = 'password_reset_email.txt'
                                        c =  {
                                        'email': user.username,
                                        'domain': 'idamm.com.co',
                                        'site_name':'idam',
                                        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                                        'user': user,
                                        'token': default_token_generator.make_token(user),
                                        'protocol':'https',
                                        }
                                        email = render_to_string(email_template_name, c)
                                        try:
                                                send_mail(subject, email, 'admin@idam.com', [user.username], fail_silently=False)
                                        except BadHeaderError:
                                                return HttpResponse('Invalid header found.')
                                        return redirect('/PasswordReset/Done/')
        password_reset_form = PasswordResetForm()
        return render(request, 'password_reset.html', {'password_reset_form':password_reset_form})

def AnaliticaAvanzada(request):
        return render(request,"AnaliticaAvanzada.html")

def IngenieroDatos(request):
        return render(request,"IngenieroDatos.html")

def FormacionCapacitacion(request):
        return render(request,"FormacionCapacitacion.html")

def LaboratorioData(request):
        return render(request,"LaboratorioData.html")

