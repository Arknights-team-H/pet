from django.urls import path

from . import views

app_name = 'breeder'
urlpatterns = [
    path('', views.NotHomeView.as_view(), name="nothome"),
    path('index', views.IndexView.as_view(), name="index"),
]