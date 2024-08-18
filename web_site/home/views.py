from django.shortcuts import render
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
# Create your views here.
