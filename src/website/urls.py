from django.urls import path, include
from . import views

# needed for include function to work in mycv/url.py for the namespace
app_name = "website"

urlpatterns = [
    path('', views.home, name="home"),
    path('test/', views.test, name="test"),
    path('login/', views.login, name="login"),
    path('edit/', views.edit, name="edit"),
    path('presentation/', views.presentation, name="presentation"),
]