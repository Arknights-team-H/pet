import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vaccination
from .models import MasterVaccination
from .models import Hospital
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True
#     def test_func(self):
#         dogcat = get_object_or_404(Vaccination, pk = self.kwargs['pk'])
#         return self.request.user == dogcat.user


class NotHomeView(generic.TemplateView):
    template_name = "nothome.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Vaccination
    template_name = 'detail.html'

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
