from django.db import models
from s3direct.field import S3DirectField
import uuid

# Create your models here.

class Photo(models.Model):
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False,
    )
    created_at = models.DateTimeField(auto_now_add=True) 
    title = models.CharField(max_length=100)
    photo = models.FileField()
    