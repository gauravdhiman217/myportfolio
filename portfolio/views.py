from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from portfolio.models import Projects , Contact
# Create your views here.

def index(request):
    if request.method == 'GET':
        forms = Projects.objects.all()
        return render(request,'index.html',{'forms':forms})
    
def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    print("===========",name,email)
    return HttpResponseRedirect("index")
