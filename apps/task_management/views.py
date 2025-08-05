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
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta
from django.utils import timezone

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

    # update user based on sessionid
    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

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


class NearDeadlineCommentsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        today = timezone.now()
        today_start = today.replace(hour=0, minute=0, second=0, microsecond=0)
        upcoming = today_start + timedelta(days=3)
        print('today time is :',today_start)
        print('Upcoming 3 day mark:', upcoming)

        near_deadline_projects = Project.objects.filter(
           dueDate__lte= upcoming,
           dueDate__gte = today_start
        )

        comments = ProjectComment.objects.filter(project__in= near_deadline_projects)
        serializer = ProjectCommentSerializer (comments, many=True)
        return Response(serializer.data)

from apps.task_management.models import ShotAssociation
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Max, Q

class ArtistShotStatsAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.email  # You can adjust to use query params if needed
        stats = get_artist_latest_shot_stats(user_id)
        return Response(stats)

def get_artist_latest_shot_stats(user_id):
    # Find latest version of each shot assigned to this user
    latest_versions = (
        ShotAssociation.objects
        .filter(user__email=user_id)
        .values('shot_id')
        .annotate(latest_version=Max('version'))
    )

    # Build a query to match each shot by latest version assigned
    filters = Q()
    for item in latest_versions:
        filters |= Q(shot_id=item['shot_id'], version=item['latest_version'], user__email=user_id)

    # Retrieve only latest assignments
    latest_assignments = ShotAssociation.objects.filter(filters)
    in_review_shots = (
        ShotAssociation.objects
        .filter(assigned_from=user_id).filter(shot__Status="IN REVIEW")
        .values('shot_id')
        .annotate(latest_version=Max('version'))
    ).count()
    stats = {
        "completed": latest_assignments.filter(shot__Status="APPROVED").count(),
        "in_progress": latest_assignments.filter(shot__Status="IN PROGRESS").count(),
        "todo_assigned": latest_assignments.filter(shot__Status="TODO").count(),
        "in_review": in_review_shots
    }
    return stats