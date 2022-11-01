import os
from django import forms
from django.core.mail import EmailMessage
from django.contrib.admin.widgets import AdminDateWidget
from .models import Vaccination
from .models import Hospital
from .models import Medicine


class CreateForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('mc_number','date','vaccination','hospital_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

