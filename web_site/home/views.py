from django.shortcuts import render

from home.models import Test


def home_page(request):
    return render(request,"home.html")
def users_page(request):
    return render(request,'users.html')
def about(request):
    return render(request,'about.html')
def calc_bmi(request):
    height = float(request.GET["height"])
    weight = int(request.GET["weight"])
    result = round((weight/height**2),2)
    answer = ""
    if 20 <= result <= 24:
        answer = "وزن مناسب"
    elif result > 24:
        answer = "چاق"
    elif result < 20:
        answer = "لاغر"
    return render(request,'bmi.html',{'result':result,'answer':answer})
def input(request):
    if request.method == 'POST':
        test = Test(full_name=request.POST['txtName'],email=request.POST['txtEmail'],balance=request.POST['txtBalance'])
        test.save()
        return render(request,'input_info.html',{'message':'information of users entered correctly'})
    return render(request,'input_info.html')
# Create your views here.
