from djongo import models
from datetime import datetime

class BlogModel(models.Model):
    _id = models.ObjectIdField()
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    date_created = models.DateTimeField(default=datetime.now()) 