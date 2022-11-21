from django.urls import path
from . import views

app_name = 'owner'
urlpatterns = [
    path('userindex', views.UserIndexview.as_view(), name="userindex"),
]
