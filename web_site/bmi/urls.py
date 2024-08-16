from django.urls import path
from . import views
urlpatterns = [
    path('bmi/',views.calc_bmi,name="bmi")
]
