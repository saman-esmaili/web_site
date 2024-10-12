import hashlib

from django.contrib.auth import authenticate, login, logout
from django.core.validators import validate_email
from django.db.models import Q
from django.shortcuts import render, redirect

from users.models import Customer, Post, Products


def index(request):
    return render(request, "users/index.html", {'id': 'page1'})


def about(request):
    return render(request, "users/about.html", {'id': 'page2'})


def courses(request):
    return render(request, "users/courses.html", {'id': 'page3'})


def recipes(request):
    return render(request, "users/recipes.html", {'id': 'page4'})


def calendar(request):
    return render(request, "users/calendar.html", {'id': 'page5'})


def contact(request):
    if request.method == 'POST':
        user = Customer(full_name=request.POST['txtName'], email=request.POST['txtEmail'])
        user.save()
        comment = Post(comment=request.POST['txtComment'], users_id=user.id)
        comment.save()
    return render(request, "users/contact.html", {'id': 'page6'})


def sign_in(request):
    if request.method == 'POST':
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'users/sign_in.html', {'id': 'page7', 'hasError': True})
    return render(request, "users/sign_in.html", {"id": "page7"})


def dashboard(request):
    return render(request, "users/dashboard.html", {"id": "page8"})


def sign_up(request):
    if request.method == "POST":
        full_name = request.POST.get('txtFullName')
        email = request.POST.get('txtEmail')
        birth_date = request.POST.get('txtBirthDate')
        gender = request.POST.get('txtGender')
        username = request.POST.get('txtUsername')
        password = request.POST.get('txtPassword')
        re_password = request.POST.get('txtRePassword')
        #   validation
        if len(full_name) < 3:
            context = {"hasError": True, "message": "your full name is Too short", "id": "page9"}
            return render(request, "users/sign_up.html", context)
        try:
            validate_email(email)
        except Exception as er:
            context = {"hasError": True, "message": str(er), "id": "page9"}
            return render(request, "users/sign_up.html", context)
        if len(username) < 8:
            context = {"hasError": True, "message": "username must have at least 8 characters", "id": "page9"}
            return render(request, "users/sign_up.html", context)
        if not password or password != re_password:
            context = {"hasError": True, "message": "your password didn't match or is empty", "id": "page9"}
            return render(request, "users/sign_up.html", context)
        tempCustomer = list(Customer.objects.filter(Q(username=username) | Q(email=email)))
        if tempCustomer:
            if tempCustomer[0].email == email:
                context = {"hasError": True, "message": "email already taken", "id": "page9"}
                return render(request, "users/sign_up.html", context)
            elif tempCustomer[0].username == username:
                context = {"hasError": True, "message": "username already taken", "id": "page9"}
                return render(request, "users/sign_up.html", context)
        customer = Customer()
        customer.fullName = full_name
        customer.email = email
        customer.birthDate = birth_date
        customer.gender = gender
        customer.username = username
        customer.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        customer.save()
        context = {"hasError": True, "message": "your registered", "id": "page9"}
        return render(request, "users/sign_up.html", context)
    return render(request, "users/sign_up.html", {"id": "page9"})


def log_out(request):
    logout(request)
    return redirect('main')


def products(request):
    search = request.GET.get('txtName')
    lowPrice = request.GET.get('lowPrice')
    highPrice = request.GET.get('highPrice')
    if not search:
        products = Products.objects.all()
        context = {'products': products}
    else:
        if lowPrice and highPrice:
            products = Products.objects.filter(Q(price__gte=highPrice)&Q(price__lte=lowPrice))
        elif lowPrice and highPrice and search:
            products = Products.objects.filter(Q(price__gt=highPrice)&Q(price__lt=lowPrice)&Q(name__contains=search))
        else:
            products = Products.objects.filter(Q(name__contains=search))
        context = {'products': products}
    return render(request, 'users/product.html', context)
