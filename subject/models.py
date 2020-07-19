from djongo import models
from datetime import datetime
from django.utils.timezone import now

class Authors(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class SubjectModel(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    date_created = models.DateTimeField(default=now)
    author = models.EmbeddedField(
        model_container = Authors
    )
    objects = models.DjongoManager()



