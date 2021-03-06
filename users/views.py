from django.shortcuts import render, redirect
from django.contrib import messages
from home import views as views_home
from .forms import UserRegisterForm

def register(request):
    if request.method== "POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            messages.success(request, f'your account has been created! you can login now')
            return redirect('login')
    else:
        form= UserRegisterForm()
    return render(request, 'users/register.html', {
    'form': form
    })
