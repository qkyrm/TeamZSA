from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms

class RegistrationView(CreateView):
    form_class = UserCreationForm
    form_class = forms.CustomRegistrationForm
    template_name = 'registration/register.html'
    success_url = '/login/'


class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def get_success_url(self):
        return redirect('/')


class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:login')


class UserListView(ListView):
    template_name = 'registration/user_list.html'
    model = User

    def get_queryset(self):
        return self.model.objects.all()

