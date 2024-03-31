from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def email_view(request):
    if request.method == 'POST':
        try:
            send_mail(
                subject=request.POST['subject'],
                message=request.POST['message'],
                from_email=EMAIL_HOST_USER,
                # from_email='info@gmail.com',
                recipient_list=[request.POST['email'], 'tohirovahmad1519@gmail.com'],
            )
            return HttpResponse('<h1>Success</h1>')
        except Exception as e:
            return HttpResponse(f'<h1>Something went wrong</h1><p>{e}</p>', status=500)
    return render(request, 'users/email.html')

