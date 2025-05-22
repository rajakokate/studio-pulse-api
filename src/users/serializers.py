from rest_framework import serializers
from .models import Department, Project, ProjectComment, Shot, ShotAssociation, Comment, User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password
# from django.contrib.auth import get_user_model
# User = get_user_model()

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [  'contact', 'email', 'role', 'dept', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        raw_password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(raw_password)  # Uses make_password internally
        user.save()
        return user

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


from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group, Permission

# Serializer for Group
class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

# Serializer for Permission
class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"
