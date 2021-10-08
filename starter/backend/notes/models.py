from django.db import models

# Create your models here.
from django.db import models


class Note(models.Model):
    content = models.TextField()
