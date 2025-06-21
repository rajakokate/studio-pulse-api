from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import  ProjectViewSet, ProjectCommentViewSet, ShotViewSet, ShotAssociationViewSet, CommentViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'projectComments', ProjectCommentViewSet)
router.register(r'shots', ShotViewSet)
router.register(r'shotAssign', ShotAssociationViewSet)
router.register(r'shotComments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
