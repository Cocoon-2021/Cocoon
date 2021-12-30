from django.shortcuts import render
from django.http import HttpResponse
from contactapp.models import *

# Create your views here.
def page(request):
    return render(request,'index.html')

def db1(request):
    if request.method=="POST":
        qtitle=request.POST['title']
        qname=request.POST['name']
        qposition=request.POST['position']
        qcompany=request.POST['company']
        qemail=request.POST['email']
        qsa1=request.POST['sa1']
        qsa2=request.POST['sa2']
        qcountry=request.POST['country']
        qcity=request.POST['city']
        qstate=request.POST['state']
        qzip=request.POST['zip']
        qtxtmobilenumber=request.POST['txtmobilenumber']
        details=table1(title=qtitle, fullname=qname, position=qposition, company=qcompany,
        email=qemail, saddr1=qsa1, saddr2=qsa2, country=qcountry,
        city=qcity, state=qstate, zip=qzip, phone=qtxtmobilenumber)
        details.save()
        return HttpResponse("Registered Succesfully")
    else:
        return render(request,'index.html')
