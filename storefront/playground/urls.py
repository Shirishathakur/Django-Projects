from django.urls import path
from . import views


urlpatterns = [
    path("hello/",views.say_hello),
    path("hello/html/",views.say_hello_html),
    path("hello/html/dict",views.say_hello_html_Siri),
    path("hello/html/condition",views.say_hello_html_conditional)
]