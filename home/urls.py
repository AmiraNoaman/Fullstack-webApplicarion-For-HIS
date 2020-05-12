from django.urls import path
from . import views
urlpatterns=[
    path('',views.index, name='index'),
    path('testing',views.PatientPrev, name='testing'),
    path('dispname',views.dispname,name ='dispname'),
    path ('disppatients', views.disppatient,name='disppatients'),
    path ('doctors', views.doctorsPrev,name='doctors'),
    path ('nurses', views.nursesPrev,name='nurses'),
    
]