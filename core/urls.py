from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="core-home"),
    path('clipboard/', views.clip,name="core-clip")

]
