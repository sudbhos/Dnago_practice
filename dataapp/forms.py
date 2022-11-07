from django import forms

class Information(forms.Form):
    name=forms.CharField()
    surname=forms.CharField()
    marks=forms.IntegerField()
