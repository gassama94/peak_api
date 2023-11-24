from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from .models import Todo

# Create your views here.
class TodView(viewsets.ModelViewSet):
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()
