import os
from django import forms
from django.core.mail import EmailMessage
from django.contrib.admin.widgets import AdminDateWidget
from .models import Vaccination


class CreateForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

