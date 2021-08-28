from event.models import Event, Student
from django.shortcuts import render,redirect
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'events/index.html')


def events(request):
    event_list = Event.objects.all()
    return render(request,'events/index.html',{
        'event_list' : event_list
    })

def dashboard(request):
    return render(request,'events/dashboard.html')


def event_details(request,event_id):
    event = Event.objects.get(pk=event_id)
    count = Student.objects.filter(event=event).count()
    return render(request,'events/details.html',{
        "event" : event,
        "count" : count
    })


def register(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        college = request.POST['college']
        gender = request.POST['gender']
        email = request.POST['email']
        phone = request.POST['phone']
        sem = request.POST['sem']
        student = Student(name=name,age=age,college=college,gender=gender,event=event,email=email,phone=phone,semester=sem)
        student.save()
        messages.success(request,("Registeresd successfully"))
        return redirect('home')
    else:
        return render(request,'events/register.html',{
            "event" : event
        })

def update_events(request):
    events = Event.objects.all()
    return render(request,'events/update_events.html',{
        "events" : events
    })

def edit_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    if request.method == "POST":
        event.name = request.POST['name']
        event.event_date = request.POST['event_date']
        event.venue = request.POST['venue']
        event.image = request.POST['event_image']
        event.description = request.POST['description']
        event.save()
        messages.success(request,("Event edited successfully"))
        return redirect('update_events')
    return render(request,'events/edit_event.html',{
        "event" : event
    })

def create_event(request):
    if request.method == "POST":
        name = request.POST['name']
        event_date = request.POST['event_date']
        venue = request.POST['venue']
        description = request.POST['description']
        image = request.POST['event_image']
        event = Event(name=name,event_date=event_date,venue=venue,description=description,image=image)
        event.save()
        messages.success(request,("Event added successfully"))
        return redirect('dashboard')
    else:
        return render(request,'events/create.html',{})


    
def delete_event(request,event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('update_events')

def data_students(request):
    students = Student.objects.all()
    return render(request,'events/data_students.html',{
         "students" : students
    })