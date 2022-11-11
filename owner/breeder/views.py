from django.views import generic

class NotHomeView(generic.TemplateView):
    template_name = "nothome.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"