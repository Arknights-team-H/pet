import logging
from django.urls import reverse_lazy
from django.views import generic
from .forms import CreateForm, InquiryForm
from django.contrib import messages
from django.db.models import Q #検索機能で使う
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Vaccination
from .models import MasterVaccination
from .models import MasterHospitalUser
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

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm

class OinquiryView(generic.TemplateView):
    template_name = "oinquiry.html"





class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Vaccination
    # template_name = 'detail.html'
    print(5)
    def display(request):
        template_name = "detail.html"
        ctx = {}
        qs = VaccinationModel.objects.all()
        ctx["object_list"] = qs

        return render(request, template_name, ctx)


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

    # def get(self, request, *args, **kwargs):
    #     return render(request, "Vsearch.html")

    def post(self, request, *args, **kwargs):
        number = request.POST["number"]
        if Vaccination.objects.filter(mc_number__iexact=number):
            return render(request, "detail.html")
        else:
            return render(request, "Vsearch.html")
        messages.add_message(request, messages.INFO, "一致する値が見つかりません ")



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



