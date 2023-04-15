from django.urls import path
from . import views

urlpatterns = [
    path('', views.Logged, name='users'),
    path('Logout', views.Logout, name='logout')
]
