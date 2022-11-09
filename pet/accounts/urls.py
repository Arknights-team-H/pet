from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('Hospitalcreate/', views.HospitalCreateView.as_view(), name="Hospitalcreate"),
]