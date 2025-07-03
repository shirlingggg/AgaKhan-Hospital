from django.shortcuts import render, redirect
from myapp.models import *
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def doctors(request):
    return render(request, 'doctors.html')

def appointment(request):
    if request.method== "POST":
        myappointments =Appointment(
            name= request.POST['name'], #first "name" from the model, second one from the html file in the name attribute
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']


        )
        myappointments.save()
        messages.success(request, 'Your appointment has been submitted successfully!')
        return redirect('/appointment')
    else:

        return render(request, 'appointment.html')




def departments(request):
    return render(request, 'departments.html')

def contact(request):
    if request.method == "POST":
        mycontact = Contact(
            name=request.POST['name'],
            # first "name" from the model, second one from the html file in the name attribute
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']

        )
        mycontact.save()
        messages.success(request, 'Your message has been submitted successfully!')
        return redirect('/contact')
    else:

        return render(request, 'contact.html')




