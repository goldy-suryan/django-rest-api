from djongo import models
from datetime import datetime

class SubjectModel(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=datetime.now())