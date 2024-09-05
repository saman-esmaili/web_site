from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from users.models import Customer, Post


def index(request):
    return render(request, "users/index.html",{'id':'page1'})

def about(request):
    return render(request,"users/about.html",{'id':'page2'})

def courses(request):
    return render(request,"users/courses.html",{'id':'page3'})

def recipes(request):
    return render(request,"users/recipes.html",{'id':'page4'})
def calendar(request):
    return render(request,"users/calendar.html",{'id':'page5'})

def contact(request):
    if request.method == 'POST':
        user = Customer(full_name=request.POST['txtName'],email=request.POST['txtEmail'])
        user.save()
        comment = Post(comment=request.POST['txtComment'], users_id=user.id)
        comment.save()
    return render(request,"users/contact.html",{'id':'page6'})

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'users/sign_in.html',{'id':'page7','hasError':True})
    return render(request,"users/sign_in.html",{"id":"page7"})


def dashboard(request):
    return render(request,"users/dashboard.html",{"id":"page8"})