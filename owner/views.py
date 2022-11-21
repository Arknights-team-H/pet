import logging
import hashlib
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect

class UserIndexview(generic.TemplateView):
    template_name = "userindex.html"
