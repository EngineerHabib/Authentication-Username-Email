from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'email','password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i_name, i in self.fields.items():
            i.widget.attrs['class'] = 'form-control'

class AuthForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password']

        widgets ={
            'username': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'password': forms.PasswordInput(attrs={
                'class':'form-control'
            })
        }