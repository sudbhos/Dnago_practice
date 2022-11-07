from django.shortcuts import render,HttpResponse
from .models  import employee
from . import forms
# from django import forms

# Create your views here.
def viewsinfor(request):
    my_details=employee.objects.all()
    my_dict={"my_details":my_details}
    return render(request,'index.html',context=my_dict)

def forminfo(request):
    obj=forms.Information()
    return render(request,"home.html",{"obj":obj})