from django.contrib import admin

# Register your models here.
from .models import Department, Project, ProjectComment, Shot, ShotAssociation, Comment, User
# from django.contrib.auth import get_user_model
# User = get_user_model()
admin.site.register(Department)
admin.site.register(User)
admin.site.register(Project)
admin.site.register(ProjectComment)
admin.site.register(Shot)
admin.site.register(ShotAssociation)
admin.site.register(Comment)