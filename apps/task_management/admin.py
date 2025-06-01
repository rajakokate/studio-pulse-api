from django.contrib import admin

# Register your models here.
from .models import  Project, ProjectComment, Shot, ShotAssociation, Comment
# from django.contrib.auth import get_user_model
# User = get_user_model()
admin.site.register(Project)
admin.site.register(ProjectComment)
admin.site.register(Shot)
admin.site.register(ShotAssociation)
admin.site.register(Comment)