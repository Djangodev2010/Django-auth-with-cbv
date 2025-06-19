from django.shortcuts import render
from django.views.generic import *
from .forms import *
from django.contrib.auth.views import LoginView

# Create your views here.

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegistrationForm
    success_url = 'login'
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        
        return super().form_valid(form)

class UserLoginView(LoginView):
    template_name = 'login.html'

class HomeView(TemplateView):
    template_name = 'index.html'
