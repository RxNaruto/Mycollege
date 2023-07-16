from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    files = models.FileField(upload_to='uploads/', blank=True)  # Use the files field for multiple file uploads
    file_type = models.CharField(max_length=255)
    tech_stack = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='project_files/')

    def __str__(self):
        return self.title
