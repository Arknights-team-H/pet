from django.urls import path
from . import views

app_name = 'dogcat'
urlpatterns = [
    path('', views.NotHomeView.as_view(), name="nothome"),
    path('index', views.IndexView.as_view(), name="index"),
    path('detail/<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('update/<int:pk>/', views.UpdateView.as_view(), name="update"),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name="delete"),
    path('create/', views.CreateView.as_view(), name="create"),
    path('Vsearch/', views.VsearchView.as_view(), name="Vsearch"),
    path('detail/', views.DetailView.as_view(), name="detail"),
    path('delete/', views.DeleteView.as_view(), name="delete"),
    path('update/', views.UpdateView.as_view(), name="update"),
]