from urllib import response
from django.shortcuts import render
from .models import Certificates, Contacts, Projects
from django.shortcuts import HttpResponse
# Create your views here.


def home(request):
    obj=Projects.objects.all()
    cer=Certificates.objects.all()
    con=Contacts.objects.all()
    return render(request,"home.html",{"obj":obj,"cer":cer,"con":con})

