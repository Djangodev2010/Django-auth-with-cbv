from django.urls import path
from .views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', UserLoginView.as_view(template_name='login.html'), name='login'),
    path('', HomeView.as_view(), name='index')
    
]

