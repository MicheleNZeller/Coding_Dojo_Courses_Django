from django.shortcuts import render, redirect
from .models import CourseTime

def index(request):
    print CourseTime.objects.all()
    context={
        'populate_all': CourseTime.objects.all()
    }
    return render(request, "first_app/index.html", context)

def populate(request):
    if request.method =='POST':
        print request.POST
        CourseTime.objects.create(names = request.POST['names'], description = request.POST['description'])
    return redirect('/')

def remove(request, id):
    print id
    courseTime = CourseTime.objects.get(id=id)
    context ={
        'C': courseTime,
    }
    # this = CourseTime.objects.get(id=id)
    # this.delete()
    return render(request, "first_app/destroy.html", context)

def removethis(request, id):
    if request.method == 'POST':
        this = CourseTime.objects.get(id=id)
        this.delete()
        return redirect('/')
