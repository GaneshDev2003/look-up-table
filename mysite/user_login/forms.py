from django import forms
from .models import UserLogin

class UserForm(forms.ModelForm):
    class Meta:
        model = UserLogin
        fields = ['username','password','isEditor']
