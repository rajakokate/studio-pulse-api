from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import FoodItem, Department, User, Project, ProjectComment, Shot, ShotAssociation, Comment
from .serializers import (
    DepartmentSerializer,
    UserSerializer,
    ProjectSerializer,
    ProjectCommentSerializer,
    ShotSerializer,
    ShotAssociationSerializer,
    CommentSerializer
)

# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the poll index.")

class FoodListView(APIView):
    def get(self, request):
        data = list(FoodItem.objects.values())
        return HttpResponse(data)
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCommentViewSet(viewsets.ModelViewSet):
    queryset = ProjectComment.objects.all()
    serializer_class = ProjectCommentSerializer

class ShotViewSet(viewsets.ModelViewSet):
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer

class ShotAssociationViewSet(viewsets.ModelViewSet):
    queryset = ShotAssociation.objects.all()
    serializer_class = ShotAssociationSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

from django.shortcuts import render

def create_department_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        
        # Save to DB
        Department.objects.create(name=name, description=description)

        return render(request, 'create_department.html', {'success': True})

    return render(request, 'create_department.html')


def create_user_view(request):
    if request.method == "POST":
        userName = request.POST.get('userName')
        dept = request.POST.get('dept')
        userId = request.POST.get('userId')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        
        # Save to DB
        Department.objects.create(userName=userName, userId=userId, contact=contact, dept=dept,email=email)

        return render(request, 'create_user.html', {'success': True})

    return render(request, 'create_user.html')