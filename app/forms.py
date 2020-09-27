from django import forms

from django.core import validators

class Form(forms.Form):
    name=forms.CharField(max_length=39,validators=[validators.MaxLengthValidator(6)])
    number=forms.IntegerField(validators=[validators.MaxValueValidator(11)])
    phone=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])