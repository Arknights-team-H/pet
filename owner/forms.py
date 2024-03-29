from django import forms
from dogcat.models import Medicine
from dogcat.models import MasterHospital
from dogcat.models import Vaccination
import os
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('taking_date','medicine_type',)
        widgets = {
             'taking_date': DateInput(),
         }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

class PrefectureForm(forms.ModelForm):
    class Meta:
        model = MasterHospital
        fields = ('address',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

class VerificationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('mc_number', 'owner_name',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
