from django.contrib import admin

# Register your models here.
from .models import Department, User
# from django.contrib.auth import get_user_model
# User = get_user_model()
admin.site.register(Department)
admin.site.register(User)
