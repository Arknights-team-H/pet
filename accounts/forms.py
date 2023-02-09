from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from allauth.socialaccount.forms import SignupForm
from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class MySignupForm(UserCreationForm,forms.ModelForm):
    class Meta:
        model = MyUser
        fields = (
            'username',
            'email',
            'mc_number',
            'user_birthday',
            'pet_name',
            'pet_birthday',
           )
        widgets = {
            'user_birthday': forms.SelectDateWidget(years=[x for x in range(1900, 2030)]),
            'pet_birthday': forms.SelectDateWidget(years=[x for x in range(1900, 2030)]),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

class CustomSignupForm(SignupForm):
    def validate_unique_email(self, value):
        try:
            return super(SignupForm, self).validate_unique_email(value)
        except forms.ValidationError:
            raise forms.ValidationError("既に同じメールアドレスが登録済みです。別のメールアドレスを登録お願いします。")