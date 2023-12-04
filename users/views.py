from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render
class Register(View):
    template_name = 'registration/register.html'

class Form (View):
    template_name= 'fill the form / form.html '

    def get(self, request):
        content = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, content)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form':form

        }
        return render(request, self.template_name, context)

