from django import forms
from .models import EntriesModel

class EntryForm(forms.ModelForm):
    class Meta:
        model = EntriesModel
        fields=['name','age','country','company','branch','batch']
