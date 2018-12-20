from django import forms
from django.contrib.auth.models import User
from pharmacy.models import Pharmacy, Drug

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class UserFormForEdit(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PharmacyForm(forms.ModelForm):
    class Meta:
        model = Pharmacy
        fields = ('name', 'phone', 'adress', 'logo')

class DrugForm(forms.ModelForm):
    class Meta:
        model = Drug
        #fields = ('name', 'short_descr', 'image', 'price_sell')
        fields = '__all__'
