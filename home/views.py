from django.http import HttpResponse
from django.shortcuts import render
from .models import Patient
def index (request):
    return render(request,'home/homepage.html',{})
# Create your views here.
def PatientPrev(request):
    data=Patient.objects.all()
    context={
        'var':data,
    }
     
    return render(request,'home/testing.html',context)

def disppatient(request):
    f=Patient.objects.all()
    context={
        'g':f,
    }
    return render (request,'home/disppatients.html',context)
    dispname: dispname


def dispname(request):
        if request.method=='POST' :
            x=request.POST['Patient Name']
            p=patient(PatientName=x)
            p.save()
            return HttpResponse("POST")
        else:    
            c=Patient.objects.all()
            context={
                 'x':c,
                 }
            return render(request,'home/dispname.html',context)



def doctorsPrev(request):
    data = Patient.objects.all()
    context = {
        'var': data
    }
    return render(request,'home/doctors.html',context)

def nursesPrev(request):
    data = Patient.objects.all()
    context = {
        'var': data
    }
    return render(request,'home/nurses.html',context)
