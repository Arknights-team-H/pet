import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import HospitalCreateForm
from .models import HospitalUser

class HospitalCreateView(generic.CreateView):
    model = HospitalUser
    template_name = 'signup.html'
    form_class = HospitalCreateForm
    success_url = reverse_lazy('dogcat:index')





