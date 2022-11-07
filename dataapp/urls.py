
from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.viewsinfor,name="viewsinfor"),
    path("home",views.forminfo,name="forminfo")

]
