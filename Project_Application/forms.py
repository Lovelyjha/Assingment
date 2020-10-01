from django import forms
from Project_Application.models import Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model=Manager
        fields='__all__'

