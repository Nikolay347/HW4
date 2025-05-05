#course
from django.db import models

class Course(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name