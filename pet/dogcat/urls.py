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
    path('login/', views.LoginView.as_view(), name="login"),
    path('signup/', views.SignupView.as_view(), name="signup"),
    path('vaccination/', views.VaccinationView.as_view(), name="vaccination"),
]