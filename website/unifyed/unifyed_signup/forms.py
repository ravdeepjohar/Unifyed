from django import forms
from unifyed_signup.models import Person
from django.forms import ModelForm

class SignupForm(forms.ModelForm):

    class Meta:
        model = Person
   