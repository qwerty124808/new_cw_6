from django.views.generic import (ListView, 
                                  DetailView, 
                                  TemplateView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from users.models import User
from users.forms import UserRegisterForm

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:login")
