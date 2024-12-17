from django.shortcuts import render , HttpResponse
from datetime import datetime
from Home.models import Contact
# Create your views here.


def index(request):
    context={

        'variable':'this is a sent'
    }
    return render(request , 'index.html', context)

def about(request):
    return render(request , 'about.html')
    # return HttpResponse("this is about ")

def services(request):
    return render(request , 'services.html')
    # return HttpResponse("this is service")



def contacts(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email , Phone=Phone , desc=desc,date =datetime.today())
        contact.save()

    return render(request, 'contacts.html')

    
    
    
    # return HttpResponse("this is contact")

