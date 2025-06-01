from rest_framework import serializers
from .models import  Project, ProjectComment, Shot, ShotAssociation, Comment
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
# from django.contrib.auth import get_user_model
# User = get_user_model()
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectComment
        fields = '__all__'

class ShotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shot
        fields = '__all__'

class ShotAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShotAssociation
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
