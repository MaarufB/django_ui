from django.urls import path
from . import views

app_name = 'form_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_name/', views.get_name, name='get_name'),
    path('contact_me/', views.contact_me, name='contact_me'),
]