#student
from django.db import models


class Student(models.Model):
    class Meta:
        db_table = "it_students"

    name = models.CharField(max_length=255, null=False)
    completed_lessons = models.IntegerField()
    birth_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name
