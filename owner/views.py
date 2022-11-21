from django.views import generic

class NotHomeView(generic.TemplateView):
    template_name = "nothome.html"

class UserindexView(generic.TemplateView):
    template_name = "userindex.html"

class DrugView(generic.TemplateView):
    template_name = "drug.html"

class Drug_createView(generic.TemplateView):
    template_name = "drug_create.html"

class StoreView(generic.TemplateView):
    template_name = "store.html"

class UserloginView(generic.TemplateView):
    template_name = "userlogin.html"

class UsersignupView(generic.TemplateView):
    template_name = "usersignup.html"

class UserlogoutView(generic.TemplateView):
    template_name = "userlogout.html"
