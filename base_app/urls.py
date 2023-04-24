from django.urls import path
from . import views

urlpatterns = [
    path('quienesomos/', views.QuienesSomos, name='quienesomos'),
    path('contactanos/', views.index, name='contactanos'),
    path('AnaliticaAvanzada/', views.AnaliticaAvanzada, name='AnaliticaAvanzada'),
    path('IngenieroDatos/', views.IngenieroDatos, name='IngenieroDatos'),
    path('FormacionCapacitacion/', views.FormacionCapacitacion, name='FormacionCapacitacion'),
    path('LaboratorioData/', views.LaboratorioData, name='LaboratorioData'),
    path('SignIn/', views.SignIn, name='SignIn'),
    path('Register/', views.Register, name='Register'),
    path('', views.Home, name='home'),


]
