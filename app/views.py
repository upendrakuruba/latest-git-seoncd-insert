from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def contact(request):
    post=contactus.objects.all()
    return render(request,'second.html',{'post':post})

def cont(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        image=request.FILES.get('image')
        k=contactus(name=name,email=email,message=message,image=image)
        k.save()
    return render(request,'first.html')