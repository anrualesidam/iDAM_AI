from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect


def Logged(request):
    return render(request, 'logged.html', {}) #Load of success page

def Logout(request):
        logout(request)
       # messages.success(request, "Saliste con éxito")
        return redirect('home')
