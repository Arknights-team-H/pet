from .models import HospitalUser
from django.contrib.auth.forms import UserCreationForm

class MysignupForm(UserCreationForm):
    class Meta:
        model = HospitalUser
        fields = (
            # 'username',
            'email',
            # 'hospital_id',
            'hospital_name',
            'address',
            'phone_number',
            'director_name',
        )
# class MyLoginForm(UserCreationForm):
#     class Meta:
#         model = HospitalUser
#         fields = (
#             'hospital_id',
#         )