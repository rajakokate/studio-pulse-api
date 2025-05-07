from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodItem

# Create your views here.
# def index(request):
    # return HttpResponse("Hello world. You're at the poll index.")

class FoodListView(APIView):
    def get(self, request):
        data = list(FoodItem.objects.values())
        return Response(data)