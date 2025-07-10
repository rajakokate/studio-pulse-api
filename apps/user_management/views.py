from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import viewsets
from django.contrib.auth import login, logout
from rest_framework import status, permissions
from django.middleware.csrf import get_token
from .models import Department, User
from django.views.decorators.csrf import csrf_exempt
from apps.core.security_manager import IsAuthenticated, PublicReadOnly
from .serializers import (
    DepartmentSerializer,
    UserSerializer,
    GroupSerializer,
    PermissionSerializer,
    UserRegisterSerializer,
)

class DepartmentViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    permission_classes = [PublicReadOnly]
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterView(APIView):
    @csrf_exempt
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


class SessionLogoutView(APIView):
    permission_classes = [IsAuthenticated]  # or [permissions.AllowAny] if SECURITY_ENABLED is False
    def post(self, request):
        logout(request)  # Clears the session
        response = Response({"message": "Logout successful."}, status=status.HTTP_200_OK)
        response.delete_cookie("csrftoken")  # Optional: removes CSRF cookie
        return response

# ------------------ Get Current Logged-In User ------------------
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

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
    permission_classes = [PublicReadOnly]  # Allow unrestricted GET
    #permission_classes = [IsAuthenticated]  # Restrict access as needed

# Permission ViewSet
class PermissionViewSet(ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [PublicReadOnly]
    #permission_classes = [IsAuthenticated]  # Restrict access as needed


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
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)

# --------------- Health checkup for testing ----------------
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({"status": "healthy"})
print("Thankyou") 