from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('', views.NotHomeView.as_view(), name="nothome"),
    path('userindex/', views.UserindexView.as_view(), name="userindex"),
    path('drug/', views.DrugView.as_view(), name="drug"),
    path('drug/<int:year>/<int:month>/', views.DrugView.as_view(), name="drug"),
    path('drug_create/', views.Drug_createView.as_view(), name="drug_create"),
    path('Ssearch/', views.SsearchView.as_view(), name="Ssearch"),
    # path('store/', views.StoreView.as_view(), name="store"),
    # path('userlogin/', views.UserloginView.as_view(), name="userlogin"),
    # path('usersignup/', views.UsersignupView.as_view(), name="usersignup"),
    path('userlogout/', views.UserlogoutView.as_view(), name="userlogout"),
    path('certificate/', views.CertificateView.as_view(), name="certificate"),
]
