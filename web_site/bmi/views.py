from django.shortcuts import render
def calc_bmi(request):
    height = int(request.GET["a"])
    weight = int(request.GET["b"])
    result = weight/height**2
    answer = ""
    if 20 <= result <= 24:
        answer = "وزن مناسب"
    elif result > 24:
        answer = "چاق"
    elif result < 20:
        answer = "لاغر"
    return render(request,'bmi.html',{'result':result,'answer':answer})
# Create your views here.
