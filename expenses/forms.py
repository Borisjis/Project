from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Review




class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=200,
        required = True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
    )
    email = forms.EmailField(
        max_length=100,
        required = False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
    )
    password1 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        required = True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
    )
    check = forms.BooleanField(required = True)

    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2', 'check',
        ]
        

class expenseForm(forms.Form):
    expenseName = forms.CharField()
    expenseAmount = forms.IntegerField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']