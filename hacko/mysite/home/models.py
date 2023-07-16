from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

# Create your models here.
class Signup(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='signup_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='signup_user_permissions')
    class Meta:
        verbose_name = 'Signup'
        verbose_name_plural = 'Signups'
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    name = models.CharField(max_length=150)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username