from dataclasses import field
import imp
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from myApp.models import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
class MyBooks(ModelForm):
    class Meta:
        model = books
        widgets = {
            'decriptions': forms.Textarea(attrs={'rows':12, 'cols':53}),
            }
        fields = ['authorName', 'bookName', 'decriptions', 'pages', 'releaseDate', 'category', 'avatar', 'price']
class ReviewForm(forms.ModelForm):
	class Meta:
            model = ProductReview
            widgets = {
            'review_text': forms.Textarea(attrs={'rows':3, 'cols':6}),
            }
            
            fields=['review_text','review_rating']
class CartItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'address']