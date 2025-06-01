from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import  ProjectViewSet, ProjectCommentViewSet, ShotViewSet, ShotAssociationViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'comments', ProjectCommentViewSet)
router.register(r'shots', ShotViewSet)
router.register(r'shotAssign', ShotAssociationViewSet)
router.register(r'shots', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
