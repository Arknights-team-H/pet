from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .forms import MedicineForm
from dogcat.models import Medicine
from dogcat.models import MasterHospital
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class NotHomeView(generic.TemplateView):
    template_name = "nothome.html"
class UserindexView(generic.TemplateView):
    template_name = "userindex.html"
class DrugView(LoginRequiredMixin,generic.TemplateView):
    template_name = "drug.html"
class Drug_createView(generic.FormView):
    template_name = "drug_create.html"
    form_class = MedicineForm
    model = Medicine
class SsearchView(generic.ListView):
    model = MasterHospital
    template_name = "Ssearch.html"
    success_url = reverse_lazy('owner:Ssearch')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            prefectures = request.POST.get('prefectures')

            def get_queryset(self):
                hospitals = MasterHospital.objects.filter(address=prefectures).order_by('-created_at')
                return hospitals


class StoreView(generic.TemplateView):
    template_name = "store.html"

# class UserloginView(generic.TemplateView):
#     template_name = "userlogin.html"
# class UsersignupView(generic.TemplateView):
#     template_name = "usersignup.html"
class UserlogoutView(generic.TemplateView):
    template_name = "userlogout.html"