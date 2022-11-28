from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from allauth.socialaccount.forms import SignupForm


class MySignupForm(UserCreationForm):
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

class CustomSignupForm(SignupForm):
    def validate_unique_email(self, value):
        try:
            return super(SignupForm, self).validate_unique_email(value)
        except forms.ValidationError:
            raise forms.ValidationError("既に同じメールアドレスが登録済みです。別のメールアドレスを登録お願いします。")