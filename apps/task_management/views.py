from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import  permissions
from .models import Project, ProjectComment, Shot, ShotAssociation, Comment
from apps.core.security_manager import IsAuthenticated, PublicReadOnly
from .serializers import (
    ProjectSerializer,
    ProjectCommentSerializer,
    ShotSerializer,
    ShotAssociationSerializer,
    CommentSerializer,
)
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the poll index.")


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectCommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ProjectComment.objects.all()
    serializer_class = ProjectCommentSerializer

class ShotViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Shot.objects.all()
    serializer_class = ShotSerializer

class ShotAssociationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ShotAssociation.objects.all()
    serializer_class = ShotAssociationSerializer

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
