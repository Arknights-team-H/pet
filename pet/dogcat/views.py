import logging
import hashlib
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateForm, ApplyForm, LoginForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vaccination
from .models import MasterVaccination
from .models import MasterHospitalUser
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)


class IndexView(generic.TemplateView):
    template_name = "index.html"

class ApplyView(generic.FormView):
    template_name = "apply.html"
    form_class = ApplyForm
    success_url = reverse_lazy('dogcat:login')

    def form_valid(self, form):
        dogcat = form.save(commit=True)
        messages.success(self.request, 'データベースに登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(1)
        messages.error(self.request, "データベースの登録に失敗しました。")
        return super().form_invalid(form)


class CapplyView(generic.FormView):
    template_name = "Capply.html"
    form_class = ApplyForm
    success_url = reverse_lazy('dogcat:login')

class InquiryView(generic.TemplateView):
    template_name = "inquiry.html"


class CreateView(generic.CreateView):
    model = Vaccination
    template_name = 'create.html'
    form_class = CreateForm
    success_url = reverse_lazy('dogcat:index')

    def form_valid(self, form):
        print("djfslkjklsd")
        dogcat = form.save(commit=True)
        # dogcat.user = self.request.user
        # dogcat.save()
        messages.success(self.request, 'データベースを登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(1)
        messages.error(self.request, "データベースの登録に失敗しました。")
        return super().form_invalid(form)


class UpdateView(generic.UpdateView): # UpdateViewクラスを継承している
    model = Vaccination
    template_name = 'update.html'
    form_class = CreateForm
    def get_success_url(self): # オーバーライド
        return reverse_lazy('dogcat:detail', kwargs = {'pk': self.kwargs['pk']})

    def form_valid(self, form): # 更新が成功した時の処理。formはユーザが入力したのが入っている。オーバーライド。
        messages.success(self.request, "データベースを更新しました。")
        return super().form_valid(form)

    def form_invalid(self, form): # オーバーライド
        messages.error(self.request, "データベースの更新に失敗しました。")
        return super().form_invalid(form)


class DeleteView(generic.DeleteView):
    model = Vaccination
    template_name = 'delete.html'
    success_url = reverse_lazy('dogcat:SearchResults')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "データを削除しました。")
        return super().delete(request, *args, **kwargs)


class VsearchView(generic.FormView):
    model = Vaccination
    form_class = CreateForm
    template_name = 'Vsearch.html'
    # success_url = reverse_lazy('dogcat:vaccination')
    def get_queryset(self):
        try:
            q = self.request.GET["search"]
        except:
            q = None
        return VaccinationModel.objects.search(query=q)


class DetailView(generic.FormView):
    model = Vaccination
    form_class = CreateForm
    template_name = 'detail.html'
    # success_url = reverse_lazy('dogcat:vaccination')

class DeleteView(generic.FormView):
    model = Vaccination
    form_class = CreateForm
    template_name = 'delete.html'
    # success_url = reverse_lazy('dogcat:vaccination')

class UpdateView(generic.FormView):
    model = Vaccination
    form_class = CreateForm
    template_name = 'update.html'
    # success_url = reverse_lazy('dogcat:vaccination')

class LoginView(generic.FormView):
    model = MasterHospitalUser
    form_class = LoginForm
    template_name = 'login.html'
    flag = 5
    if flag == 0:
        success_url = reverse_lazy('dogcat:index')
    else:
        success_url = reverse_lazy('dogcat:login')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # フォーム入力のユーザーID・パスワード取得
            hospital_id = request.POST.get('hospital_id')
            Password = request.POST.get('password')
            password = hashlib.sha256(Password.encode()).hexdigest()
            print(hospital_id)
            print(password)
            if MasterHospitalUser.objects.filter(hospital_id=hospital_id, password=password):
                flag = 0
                print(1)
            else:
                flag = 1
                print(2)
            obj = flag
            # obj.save()
            # messages.success(self.request, 'データベースを登録しました。')
            return super().post(obj)

class UserAddView(generic.FormView):
    model = MasterHospitalUser
    form_class = LoginForm
    template_name = 'useradd.html'
    success_url = reverse_lazy('dogcat:login')

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # フォーム入力のユーザーID・パスワード取得
            hospital_id = request.POST.get('hospital_id')
            Password = request.POST.get('password')
            password = hashlib.sha256(Password.encode()).hexdigest()
            print(hospital_id)
            print(password)
            obj = MasterHospitalUser(hospital_id=hospital_id, password=password)
            obj.save()
            messages.success(self.request, 'データベースを登録しました。')
            return super().post(obj)

