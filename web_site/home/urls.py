from django.urls import path,include
from home import views
urlpatterns = [
    path("",views.home_page,name="home"),
    path('users/',include('users.urls')),
    path('about/',include('about.urls')),
    path('bmi/',include('bmi.urls'))
]
