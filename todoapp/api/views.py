
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser 
from todoapp.api.permissions import IsOwnerPermission
from todoapp.api.serializers import TaskSerializer
from todoapp.models import Task

class TasksListView(viewsets.ModelViewSet):
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerPermission]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)