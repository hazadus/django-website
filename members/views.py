from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  # Sign Up form for new user


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Login new user after registration:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You were successfully registered. Welcome!')
            return redirect('user_profile')
    else:
        form = UserCreationForm()
    return render(request, 'authenticate/signup.html', {
        'form': form
    })


def login_user(request):
    # https://docs.djangoproject.com/en/4.1/topics/auth/default/#how-to-log-a-user-in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Failed to log in.')
            return redirect('login_user')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, 'You were logged out.')
    return redirect('login_user')


def user_profile(request):
    return render(request, 'authenticate/profile.html', {})
