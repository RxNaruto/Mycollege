from django.urls import path
from .views import file_upload
from .views import project_list

urlpatterns = [
    path('file-upload/', file_upload, name='file_upload'),
    path('projects/', project_list, name='project_list'),


]
