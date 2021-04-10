from django import forms
from .models import *


class PersonForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, label='First name',
                                 widget=forms.TextInput(attrs={"class": "form-control",
                                                               "placeholder": "First name"}))
    last_name = forms.CharField(max_length=30, label='Last name', widget=forms.TextInput(attrs={"class": "form-control",
                                                                                                "placeholder": "Last name"}))
    age = forms.IntegerField(label='Age', widget=forms.NumberInput(attrs={"class": "form-control",
                                                                          "placeholder": "Age"}))
    country = forms.CharField(max_length=50, label='Country', widget=forms.TextInput(attrs={"class": "form-control",
                                                                                            "placeholder": "Country"}))

    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'age', 'country',)