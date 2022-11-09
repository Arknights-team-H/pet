import os
from django import forms
from django.core.mail import EmailMessage
from .models import HospitalUser
from .allauth.account.forms import SignupForm
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.forms import (SignupForm,
)
class CustomSignupForm(SignupForm):