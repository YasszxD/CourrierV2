from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from register.models import Profile, Courier


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class MyProfileCreationForm(ModelForm):
    city = forms.CharField(max_length=30)
    postal_code = forms.IntegerField(max_value=9999,min_value=1000)
    phone_number =forms.IntegerField(max_value=99999999,min_value=20000000)

    class Meta:
        model = Profile
        fields = ('city', 'postal_code', 'phone_number')


class MyCourierCreationForm(ModelForm):
    recieverFullName = forms.CharField(max_length=30, required=True)
    recieverAddress = forms.CharField(max_length=30, required=True)
    recieverPhoneNumber = forms.CharField(max_length=8, required=True)
    description = forms.CharField(max_length=300, required=True)
    weight = forms.CharField(max_length=4, required=True)
    class Meta:
        model = Courier
        fields =['recieverFullName','recieverAddress','recieverPhoneNumber','description', 'weight']
