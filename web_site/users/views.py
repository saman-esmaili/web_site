from django.shortcuts import render

from users.models import Users, Post


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
    if request.method == 'POST':
        user = Users(full_name=request.POST['txtName'],email=request.POST['txtEmail'])
        user.save()
        comment = Post(comment=request.POST['txtComment'], users_id=user.id)
        comment.save()
    return render(request,"users/contact.html")

