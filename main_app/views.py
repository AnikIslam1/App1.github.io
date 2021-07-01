from django.http import HttpResponse
from django.views.generic import TemplateView
from rest_framework import generics
from .models import Register
from .serializers import RegisterSerializer

#Page Test
# def homeView(request):
#     return HttpResponse("Hello")

#index.html link

class HomeView(TemplateView):
    template_name = "index.html"


#Rest API part Admin
class RegisterView(generics.CreateAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer

class RegisterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer



