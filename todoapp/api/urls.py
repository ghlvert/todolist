from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from todoapp.api.views import TasksListView
from todoapp.views import index, detail_task, create_task, delete_task

router = routers.SimpleRouter()
router.register(r'viewset', TasksListView)

urlpatterns = [
    path('tasks/', include(router.urls)),
    path('/auth/', include('djoser.urls')),         
    re_path(r'^auth/', include('djoser.urls.authtoken')), 
]