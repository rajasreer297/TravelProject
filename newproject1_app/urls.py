from . import  views
from django.urls import path

urlpatterns=[
    path('',views.newproject1,name='newproject1')
]