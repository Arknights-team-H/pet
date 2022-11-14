import os
from django import forms
from django.core.mail import EmailMessage
from django.contrib.admin.widgets import AdminDateWidget
from .models import Vaccination
from .models import MasterHospitalUser
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

class InquiryForm(forms.Form):
    name = forms.CharField(label='病院名', max_length=30)
    representativename = forms.CharField(label='代表者氏名', max_length=15)
    address = forms.CharField(label='住所', max_length=255)
    phonenumber = forms.IntegerField(label='電話番号')
    file = forms.ImageField(label='画像ファイル')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col-9'
        self.fields['name'].widget.attrs['placeholder'] = '病院名をここに入力してください。'

        self.fields['representativename'].widget.attrs['class'] = 'form-control col-10'
        self.fields['representativename'].widget.attrs['placeholder'] = '代表者氏名をここに入力してください。'

        self.fields['address'].widget.attrs['class'] = 'form-control col-11'
        self.fields['address'].widget.attrs['placeholder'] = '住所をここに入力してください。'

        self.fields['phonenumber'].widget.attrs['class'] = 'form-control col-12'
        self.fields['phonenumber'].widget.attrs['placeholder'] = '電話番号をここに入力してください。'

        self.fields['file'].widget.attrs['class'] = 'form-control col-13'
        self.fields['file'].widget.attrs['placeholder'] = '画像をここに添付してください。'


# 必要項目＝代表者名、画像、パソコンのipアドレス（2台or3台まで）、病院名、住所、電話番号