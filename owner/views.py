from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render


from dogcat.models import MasterHospital

class NotHomeView(generic.TemplateView):
    template_name = "nothome.html"
class UserindexView(generic.TemplateView):
    template_name = "userindex.html"
class DrugView(generic.TemplateView):
    template_name = "drug.html"
class Drug_createView(generic.TemplateView):
    template_name = "drug_create.html"
class StoreView(generic.TemplateView):
    model = MasterHospital
    template_name = "store.html"
    success_url = reverse_lazy('owner:store')
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            prefectures = request.POST.get('prefectures')
            if MasterHospital.objects.get(address__contains=prefectures):
                print(1)
                result = MasterHospital.objects.filter(address=prefectures).all()
                print(result.mc_number)
                ctx = {}
                ctx["objects"] = result
                return render(request, 'store.html', ctx)
            obj = 0
            return super().post(obj)

# class UserloginView(generic.TemplateView):
#     template_name = "userlogin.html"
# class UsersignupView(generic.TemplateView):
#     template_name = "usersignup.html"
class UserlogoutView(generic.TemplateView):
    template_name = "userlogout.html"