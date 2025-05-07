from django.urls import path
# from .views import FoodListView
from . import views
urlpatterns = [
     path("",views.index, name="index"),
     #path('food-items/', FoodListView.as_view()),
]
