from django.contrib import admin

# Register your models here.
from register.models import Profile, Courier

admin.site.register(Profile)
admin.site.register(Courier)