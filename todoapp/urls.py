from django.contrib import admin
from django.urls import path

from todoapp.views import index, detail_task, create_task, delete_task

app_name = 'todoapp'

urlpatterns = [
    path('', index, name='home'),
    path('task/<int:task_id>', detail_task, name='detail_task'),
    path('create/', create_task, name='create_task'),
    path('delete/<int:task_id>', delete_task, name='delete_task'),
]
