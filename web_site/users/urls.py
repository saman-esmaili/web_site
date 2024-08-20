from django.urls import path,include

from users import views

urlpatterns = [
    path("", views.index,name='main'),
    path("about/",views.about,name='about'),
    path("courses/",views.courses,name='courses'),
    path("recipes/",views.recipes,name='recipe'),
    path("calendar/",views.calendar,name='calendar'),
    path("contact/",views.contact,name='contact'),
]