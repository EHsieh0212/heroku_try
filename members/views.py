from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterUserForm
from django.contrib.auth.decorators import login_required


# Create your views here. #original log-in
def login_user(request):
    if request.method == "POST":        #if sb filled out the form
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  #由django檢查是否為正確的帳密
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There was an error logging in, please try again."))
            return redirect('login')
    return render(request, 'registration/login.html', {})



def logout_user(request):
    logout(request)
    messages.success(request, ("You were logged out."))
    return redirect('home')


'''
#sso authentication
@login_required
def login_user2(request):
    return redirect('home')


def logout_user2(request):
    messages.success(request, ("You were logged out."))
    return redirect('home')
'''


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  #password1: 確認的第二個密碼
            #authenticate and login
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'authenticate/register.html', {'form':form,})