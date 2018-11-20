from django.shortcuts import render
from django.views.generic import CreateView   # generic에 있는 CreateView를 가져옴
from . import forms
from django.urls import reverse_lazy

# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
    