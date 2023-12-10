from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section': 'dashboard'})
def change_password_view(request):
    if request.method == 'POST':
        messages.success(request, 'Password changed successfully.')

        return redirect('dashboard')  # Или куда-то еще, куда вы хотите перенаправить пользователя после изменения пароля


def form_view(request):
    return render(request, 'form.html')
    return render(request, 'your_template.html')
