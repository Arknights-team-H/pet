import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Dogcat
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True
    def test_func(self):
        dogcat = get_object_or_404(Dogcat, pk = self.kwargs['pk'])
        return self.request.user == dogcat.user


class IndexView(generic.TemplateView):
    template_name = "index.html"

class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Dogcat
    template_name = 'detail.html'

class CreateView(generic.CreateView):
    model = Dogcat
    template_name = 'create.html'
    form_class = CreateForm
    success_url = reverse_lazy('dogcat:index')

    def form_valid(self, form):
        dogcat = form.save(commit=False)
        dogcat.user = self.request.user
        dogcat.save()
        messages.success(self.request, 'データベースを登録しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "データベースの登録に失敗しました。")
        return super().form_invalid(form)


class UpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView): # UpdateViewクラスを継承している
    model = Dogcat
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


class DeleteView(LoginRequiredMixin, OnlyYouMixin, generic.DeleteView):
    model = Dogcat
    template_name = 'delete.html'
    success_url = reverse_lazy('dogcat:SearchResults')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "データを削除しました。")
        return super().delete(request, *args, **kwargs)


class VaccinationView(LoginRequiredMixin, OnlyYouMixin, generic.FormView):
    model = Dogcat
    template_name = 'vaccination.html'
    success_url = reverse_lazy('dogcat:vaccination')


class LoginView(LoginRequiredMixin, generic.FormView):
    model = Dogcat
    template_name = 'login.html'
    success_url = reverse_lazy('dogcat:index')


class SignupView(
    generic.FormView):
    model = Dogcat
    template_name = 'signup.html'
    success_url = reverse_lazy('dogcat:login')





