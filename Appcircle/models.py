from django.db import models
from login.models import User


class Circle(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    image = models.ImageField()
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class CircleUser(models.Model):
    circle = models.ManyToManyField(Circle)
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('mod', 'Moderator'), ('user', 'User')])
    users = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return self.circle
