from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.home_page,name="home"),
    path('users/',views.users_page,name="usersList"),
    path('about/',views.about,name="about"),
    path('bmi/',views.calc_bmi,name="bmi"),
]
