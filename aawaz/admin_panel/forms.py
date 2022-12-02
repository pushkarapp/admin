from pyexpat import model
from tkinter import Widget
from django import forms
 
from django.contrib.auth.models import User
from products.models import *
from user_management.models import *
from django.contrib.auth import authenticate
 
# create a ModelForm


class AccountAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    username = forms.CharField(
        label="Usernme *",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username *"}
        ),
    )
    class Meta:
        model = User
        fields = ("username", "password")

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data["username"]
            password = self.cleaned_data["password"]
            if not authenticate(username=username, password=password):
                raise forms.ValidationError("Invalid login")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","password","first_name", "last_name","email","is_active")
        

class UserDetailForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = UserProfile
        fields = (
            "mobile_number",
            "profile_image",
            "cover_image", 
            "date_of_birth", 
            "gender",
            "about",
            "location",
            "lavel",
            "address_line_one",
            "address_line_two",
            "pincode",
            "city",
            "state",
            "pan_number",
            "pan_verification_date",
            )
        


class CoinForm(forms.ModelForm):
    class Meta:
        model = Coin
        fields = '__all__'

class DiamondForm(forms.ModelForm):
    class Meta:
        model = Diamond
        fields = '__all__'

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = '__all__'


       
class ProductForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_image': forms.TextInput(attrs={'class': 'form-control'}),
            'product_price': forms.TextInput(attrs={'class': 'form-control'}),
            
        }