from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
import json
from . import mixins
from .forms import MedicineForm, PrefectureForm, VerificationForm
from dogcat.models import Medicine, Vaccination, MasterHospital
from accounts.models import MyUser
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import get_object_or_404
import qrcode


class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        #取得出来なかった場合は404エラー
        owner = get_object_or_404(Owner, pk=self.kwargs['pk'])
        return self.request.user == owner.user

class UserindexView(generic.TemplateView):
    template_name = "userindex.html"

class DrugView(mixins.MonthWithScheduleMixin, LoginRequiredMixin, generic.TemplateView):
    template_name = "drug.html"
    model = Medicine
    date_field = 'taking_date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class Drug_createView(generic.FormView):
    template_name = "drug_create.html"
    form_class = MedicineForm
    model = Medicine
    success_url = reverse_lazy('owner:drug')

    def form_valid(self, form):
        print("djfslkjklsd")
        dogcat = form.save(commit=True)  # データベース名
        messages.success(self.request, 'お薬情報を登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(1)
        messages.error(self.request, "お薬情報の登録に失敗しました。")
        return super().form_invalid(form)

class SsearchView(generic.FormView):
    model = MasterHospital
    form_class = PrefectureForm
    template_name = "Ssearch.html"
    success_url = reverse_lazy('owner:Ssearch')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            address = request.POST.get('address')
            if MasterHospital.objects.filter(address__contains=address):
                result = MasterHospital.objects.filter(address__contains=address)
                print(result)
                ctx = {}
                ctx["objects"] = result
                return render(request, 'store.html', ctx)
            else:
                messages.error(self.request, "該当する情報がありませんでした。")
            obj = 0
            return super().post(obj)

class StoreView(generic.TemplateView):
    template_name = "store.html"

class UserlogoutView(generic.TemplateView):
    template_name = "userlogout.html"

class CertificateView(generic.TemplateView):
    template_name = "certificate.html"
    model = Vaccination


class SecurityView(LoginRequiredMixin, generic.FormView):
    template_name = "security.html"
    model = Vaccination, MyUser
    form_class = VerificationForm
    success_url = reverse_lazy('owner:security')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            mc_number = request.POST.get('mc_number')
            owner_name = request.POST.get('owner_name')
            print(mc_number)
            print(owner_name)
            if Vaccination.objects.filter(mc_number=mc_number, owner_name=owner_name):
                print(1)
                obj = Vaccination.objects.filter(mc_number=mc_number, owner_name=owner_name).order_by("-date").first()
                print(obj)
                ctx = {}
                ctx["objects"] = obj
                return render(request, 'certificate.html', ctx)
            else:
                messages.error(self.request, "該当する情報がありませんでした。")
            obj = 0
            return super().post(obj)

class UserDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = "userdetail.html"
    model = MyUser
    pk_url_kwarg = 'id'

    def get_queryset(self):
        diaries = MyUser.objects.filter(user=self.request.user).order_by('-created_at') #公開、非公開設定
        return diaries

class Drug_DeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "userdelete.html"
    model = Medicine
    success_url = reverse_lazy('owner:drug')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "お薬情報を削除しました。")
        return super().delete(request, *args, **kwargs)

class QRcodeView(LoginRequiredMixin,generic.TemplateView):
    template_name = "certificate.html"

    def get(self, request, *args, **kwargs):
        qr = qrcode.QRCode()
        qr.add_data('http:34.231.65.248/owner/security/')
        img = qr.make_image(fill_color="black", back_color="white")
        img.show()
        img.save("sample1.png")

        return render(request, 'userindex.html')
