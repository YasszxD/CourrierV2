from django.contrib import admin
from django.urls import path, include

import register
from register import views

urlpatterns = [
    path('', views.homePage , name='home'),
    path('login', views.loginPage , name='login'),
    path('logout', views.logoutUser , name='logout'),
    path('signup', views.signupPage , name='signup'),

]
