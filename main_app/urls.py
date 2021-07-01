from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.HomeView.as_view(), name="home"),
    path("register/", views.RegisterView.as_view(), name="reg"),
    path("register/<int:pk>",views.RegisterDetail.as_view(), name="reg_pk")
]
