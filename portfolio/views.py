from django.shortcuts import render,redirect
from django.http import HttpResponse
from portfolio.models import Projects , Contact
# Create your views here.

def index(request):
    if request.method == 'GET':
        forms = Projects.objects.all()
        return render(request,'index.html',{'forms':forms})
    
def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form = Contact(Name=name,Email=email,Subject=subject,Message=message)
        form.save()
        return HttpResponse('Response submitted Successfully')