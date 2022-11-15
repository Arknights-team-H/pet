import os
from django import forms
from django.core.mail import EmailMessage
from django.contrib.admin.widgets import AdminDateWidget
from .models import Vaccination
from .models import MasterHospitalUser
from .models import HospitalApply
from .models import Medicine


class CreateForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('mc_number','date','vaccination_type','hospital_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class SelectForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('vaccination_type',)

class ApplyForm(forms.ModelForm):
    class Meta:
        model = HospitalApply
        fields = ('hospital_name','address','phone_number','director_name', 'licence_copy')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.ModelForm):
    class Meta:
        model = MasterHospitalUser
        fields = ('hospital_id','password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
