from django.shortcuts import render
from rest_framework import viewsets

from scrum.serializers import TaskSerializer
from .models import Task

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
