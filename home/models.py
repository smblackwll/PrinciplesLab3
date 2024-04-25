from django.db import models

from login.models import User


# Create your models here.

class Comment(models.Model):
    related_page = models.CharField(max_length=20)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
