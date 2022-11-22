from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class MySignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = (
            'mc_number',
            'user_birthday',
            'pet_id',
            'pet_name',
            'pet_birthday',
           )