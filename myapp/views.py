from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect('/show')
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

def show(request):
    all= Appointment.objects.all()
    return render(request, 'show.html', {'all': all})

def showcontact(request):
    allcontacts= Contact.objects.all()
    return render(request, 'showcontact.html', {'allcontacts': allcontacts})

def delete(request, id):
    myappoint=Appointment.objects.get(id=id)
    myappoint.delete()
    return redirect('/show')

def deletecontact(request, id):
    mycon=Contact.objects.get(id=id)
    mycon.delete()
    return redirect('/showcontact')

def edit(request, id):
    editappointment=get_object_or_404(Appointment, id=id)

    if request.method=="POST":
        editappointment.name= request.POST.get('name')
        editappointment.email= request.POST.get('email')
        editappointment.phone= request.POST.get('phone')
        editappointment.datetime= request.POST.get('date')
        editappointment.department= request.POST.get('department')
        editappointment.doctor= request.POST.get('doctor')
        editappointment.message= request.POST.get('message')

        editappointment.save()
        messages.success(request, 'Your appointment has been updated successfully')
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'editappointment':editappointment})



