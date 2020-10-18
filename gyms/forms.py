from django import forms
from django.contrib.auth.models import User
from .models import Gym,Class

#""""""Auth"""""""""
class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email' ,'password']

        widgets={
        'password': forms.PasswordInput(),
        }

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())



#""""""GYM"""""""""
class GymForm(forms.ModelForm):
    class Meta:
        model = Gym
        field='__all__'



#""""""Class"""""""""
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        exclude = ['gym']

        
# class GymUserForm(forms.ModelForm):
#     class Meta:
#         model =GymUser
#         exclude = ['user']
