from django.urls import path
from . import views

# define a special variable called "urlpatterns", you must spell it properly because this is what django look for
# URL Configuration
urlpatterns = [
    path(route="hello/", view=views.say_hello)
]