#  from django.shortcuts import render , HttpResponse
#  from datetime import datetime
#  from home.models import Contact
#  # Create your views here.
#  
#  
#  def index(request):
#      context={
#  
#          'variable':'this is a sent'
#      }
#      return render(request , 'index.html', context)
#  
#  def about(request):
#      return render(request , 'about.html')
#      # return HttpResponse("this is about ")
#  
#  def services(request):
#      return render(request , 'services.html')
#      # return HttpResponse("this is service")
#  
#  
#  
#  def contacts(request):
#      if request.method == "POST":
#          name=request.POST.get('name')
#          email=request.POST.get('email')
#          Phone=request.POST.get('Phone')
#          desc=request.POST.get('desc')
#          contact=Contact(name=name, email=email , Phone=Phone , desc=desc,date =datetime.today())
#          contact.save()
#  
#      return render(request, 'contacts.html')
#  
#      
#      
#      
#      # return HttpResponse("this is contact")
#  



from django.shortcuts import render, redirect
from datetime import datetime
from home.models import Contact


from django.contrib import messages



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
        # Get the data from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')  # Changed to 'phone' to match the model
        desc = request.POST.get('desc')
        
        if not desc:
            desc = "No description provided."
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        
        # Redirect after successful POST to prevent form resubmission on page refresh
          # You can replace 'success' with the actual success page URL or view name

    # Render the contact form if it's a GET request
    return render(request, 'contacts.html')


    