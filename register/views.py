from random import random

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from register import forms
from register.forms import MyUserCreationForm, MyProfileCreationForm, MyCourierCreationForm
from register.models import Profile, Courier


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    # return CourierCreation(request)

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
            # return CourierCreation(request)
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'page': page}
    return render(request, 'login.html', context)


def homePage(request):
    if request.method == 'POST':
        return redirect('search'+'/'+request.POST.get('search'))

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
            #  return CourierCreation(request)
        else:
            messages.error(request, 'An error occurred during registration')

    context = {'form': form, 'form1': profile_form}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def courierAdd(request):
    form = MyCourierCreationForm()
    if request.method == 'POST':
        form = MyCourierCreationForm(request.POST)
        if form.is_valid():
            courier = form.save(commit=False)
            if request.user.is_authenticated:
                courier.sender = request.user
                courier.price = random() * 100
                courier.save()

    context = {'form': form}
    return render(request, 'add_courrier.html', context)


def courierView(request):
    objects = Courier.objects.filter(sender=request.user);
    context = {'objects': objects}
    return render(request, 'View_courier.html', context)


def courierSearch(request, pk):

    try:
        object = Courier.objects.get(id=pk);
    except Courier.DoesNotExist:
        user = None
    context = {'object': object}
    return render(request, 'search_courier.html', context)
