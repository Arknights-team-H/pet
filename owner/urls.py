from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('', views.UserindexView.as_view(), name="userindex"),
    path('userindex/', views.UserindexView.as_view(), name="userindex"),
    path('user-detail/', views.UserDetailView.as_view(), name="user-detail"),
    path('drug/', views.DrugView.as_view(), name="drug"),
    path('drug/<int:year>/<int:month>/', views.DrugView.as_view(), name="drug"),
    path('drug_create/', views.Drug_createView.as_view(), name="drug_create"),
    path('Ssearch/', views.SsearchView.as_view(), name="Ssearch"),
    path('userlogout/', views.UserlogoutView.as_view(), name="userlogout"),
    path('security/', views.SecurityView.as_view(), name="security"),
    path('certificate/', views.CertificateView.as_view(), name="certificate"),
    path('drug_delete/<int:pk>/', views.Drug_DeleteView.as_view(), name="drug_delete"),
    path('QRcode',views.QRcodeView.as_view(),name="QRcode"),
]
