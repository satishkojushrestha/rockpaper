from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('welcome/<int:id>',views.welcome,name="welcome"),
]