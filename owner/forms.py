from django import forms
from dogcat.models import Medicine
from dogcat.models import MasterPrefectures
import os

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ('taking_date','type',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

class PrefectureForm(forms.ModelForm):
    class Meta:
        model = MasterPrefectures
        fields = ('prefectures',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'
