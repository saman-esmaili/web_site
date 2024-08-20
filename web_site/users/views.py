from django.shortcuts import render
def index(request):
    return render(request, "users/index.html")

def about(request):
    return render(request,"users/about.html")

def courses(request):
    return render(request,"users/courses.html")

def recipes(request):
    return render(request,"users/recipes.html")
def calendar(request):
    return render(request,"users/calendar.html")

def contact(request):
    return render(request,"users/contact.html")

