from django.urls import path, include
from .views import FoodListView
from . import views
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, UserViewSet, ProjectViewSet, ProjectCommentViewSet, ShotViewSet, ShotAssociationViewSet, CommentViewSet
from .views import create_department_view, create_user_view

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'comments', ProjectCommentViewSet)
router.register(r'shots', ShotViewSet)
router.register(r'shotAssign', ShotAssociationViewSet)
router.register(r'shots', CommentViewSet)

urlpatterns = [
    path("",views.index, name="index"),
    path('food-items/', FoodListView.as_view()),
    path('', include(router.urls)),
    path('create-department/', create_department_view, name='create_department'),
    path('create-user/', create_user_view, name='create_user'),
]
