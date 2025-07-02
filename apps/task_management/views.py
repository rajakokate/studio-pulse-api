from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework import  permissions
from .models import Project, ProjectComment, Shot, ShotAssociation, Comment
from apps.core.security_manager import IsAuthenticated, PublicReadOnly
from django.db.models import Count, Case, When, IntegerField, F, FloatField, ExpressionWrapper, Value
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
    queryset = Project.objects.annotate(
        total_shots=Count('shots'),
        approved_shots=Count(
            Case(
                When(shots__Status='APPROVED', then=1),
                output_field=IntegerField()
            )
        )
    ).annotate(
        completion_percentage=Case(
            When(total_shots=0, then=Value(0.0)),
            default=ExpressionWrapper(
                100.0 * F('approved_shots') / F('total_shots'),
                output_field=FloatField()
            ),
            output_field=FloatField()
        )
    )
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
