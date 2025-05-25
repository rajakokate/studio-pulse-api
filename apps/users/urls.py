from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, UserViewSet, ProjectViewSet, ProjectCommentViewSet, ShotViewSet, ShotAssociationViewSet, CommentViewSet
from .views import create_department_view, create_user_view, UserRegisterView
from .views import CurrentUserView, LogoutView, LoginView, SessionLoginView
from .views import GroupViewSet, PermissionViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'comments', ProjectCommentViewSet)
router.register(r'shots', ShotViewSet)
router.register(r'shotAssign', ShotAssociationViewSet)
router.register(r'shots', CommentViewSet)
userRoutes = DefaultRouter()
userRoutes.register(r'groups', GroupViewSet)
userRoutes.register(r'permissions', PermissionViewSet)

urlpatterns = [
    path("",views.index, name="index"),
    path('', include(router.urls)),
    path('create-department/', create_department_view, name='create_department'),
    path('create-user/', create_user_view, name='create_user'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signin/', SessionLoginView.as_view(), name='signin'),
    path('me/', CurrentUserView.as_view()),  # fetch current user info
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(userRoutes.urls)),  # Include the DRF router


]
