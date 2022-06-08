import uuid
from django.db import models
from django.utils import timezone

# Create your models here.
class Tutorials(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False, unique=True)
    body = models.CharField(max_length=100000, null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
