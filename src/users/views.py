from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
#from streamlit import status
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from rest_framework import status, permissions
from django.middleware.csrf import get_token
from .models import Department, Project, ProjectComment, Shot, ShotAssociation, Comment, User
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .serializers import (
    DepartmentSerializer,
    UserSerializer,
    ProjectSerializer,
    ProjectCommentSerializer,
    ShotSerializer,
    ShotAssociationSerializer,
    CommentSerializer,
    GroupSerializer,
    PermissionSerializer,
    UserRegisterSerializer,
)
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    return HttpResponse("Hello world. You're at the poll index.")

    
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

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render

@csrf_exempt
def create_department_view(request):
    if request.method == "POST":
        deptId = request.POST.get('deptId')
        deptName = request.POST.get('deptName')
        
        # Save to DB
        Department.objects.create(deptId=deptId, deptName=deptName)

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

# ------------------ Login ------------------
class SessionLoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)  # Sets the session
                response = Response({"message": "Login successful"}, status=status.HTTP_200_OK)
                response.set_cookie("csrftoken", get_token(request))  # Optional: expose CSRF token
                return response
        except User.DoesNotExist:
            pass

        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# ------------------ Get Current Logged-In User ------------------
class CurrentUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group, Permission
from rest_framework.permissions import IsAuthenticated


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]  # Restrict access as needed

# Permission ViewSet
class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]  # Restrict access as needed


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(email=email).first()
        if email is None:
            user = User.objects.filter(username=username).first()

        if user is not None and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            refresh["email"] = user.email
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=HTTP_400_BAD_REQUEST)
# ------------------ Logout ------------------
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)