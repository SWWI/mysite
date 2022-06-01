
from django.urls import path

from . import views
app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('myhome/', views.about, name = 'myhome'),
    path('contact/', views.contact, name = 'contact')

]