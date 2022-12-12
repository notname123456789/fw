from django.forms import ModelForm , TextInput , EmailInput
from .models import *
from django import forms

class order_f(ModelForm):
    class Meta:
        model = order
        fields = ['adress','phone']

        widgets = {
            "adress": TextInput (attrs = { 'placeholder': 'адрес'}),
            "phone" : TextInput (attrs = { 'placeholder': 'телефон'}),
            }

class code_f(ModelForm):
    class Meta:
        model = code
        fields = ['CODE']
        widgets = {
                "CODE": TextInput (attrs = { 'placeholder': 'четырехзначный код'}),
                }

class Reg_f(forms.ModelForm):  # Crée un formulaire se basant sur Action
    reg = forms.ModelChoiceField(queryset=regions.objects.all())
    class Meta:
        model = regions
        fields = ['name']