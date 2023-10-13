from django.urls import path
from csk.views import *
app_name='anything'

urlspatterns=[
    path('msd/',msd,name='msd'),
]