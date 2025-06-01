from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser
# from django.conf import settings
# ------------------ Department ------------------
class Department(models.Model):
    deptId = models.CharField(primary_key=True, max_length=100)
    deptName = models.TextField()
    description = models.TextField()

    def __str__(self):
        return self.deptNamea


# ------------------ User ------------------
# ------------------ User Manager ------------------
class User(AbstractUser):

    contact = models.TextField(blank=True, null=True)
    email = models.EmailField(primary_key=True, max_length=100)
    role = models.TextField()
    dept = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    password = models.CharField(max_length=128)  # hashed password
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions"
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["contact", "username"]
    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.userName
