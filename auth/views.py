from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import (
    LoginView, 
    LogoutView
)

class Login(LoginView):
    template_name="login.html"
    redirect_authenticated_user=True

class Logout(LogoutView):
    pass