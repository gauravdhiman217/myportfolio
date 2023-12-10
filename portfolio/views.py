from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from portfolio.models import Projects , Certification
from .forms import ContactForm
from django.contrib import messages

def index(request):
    if request.method =='POST':
        contactus_form = ContactForm(request.POST)
        if contactus_form.is_valid():
            contactus_form.save()
            messages.success(request,"Thank you for connecting, I will reach to you soon !")
            return redirect("/#contact")
        else:
            messages.error(request,"Invalid Response")
            messages.error(request,contactus_form.errors)
    contactus_form = ContactForm()
    forms = Projects.objects.all()
    certification = Certification.objects.all()
    return render(request,'index.html',{'forms':forms,'certifications':certification,'contactus_form':contactus_form})
    

