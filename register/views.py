from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from register import forms
from register.forms import MyUserCreationForm, MyProfileCreationForm
from register.models import Profile


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

      #  try:
       #     user = User.objects.get(username=username)
        #except:
         #   messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'page': page}
    return render(request, 'login.html', context)


def homePage(request):
    context = {}
    return render(request, 'main.html', context)


def signupPage(request):
    form = MyUserCreationForm()
    profile_form = MyProfileCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        profile_form = MyProfileCreationForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)

            profile = profile_form.save(commit=False)
            profile.user = user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user.save()
            profile.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form , 'form1': profile_form}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')