#
from django.db import models
from django.core.exceptions import ValidationError

class Company(models.Model):
    objects = models.Manager()      #Вказуємо явно менеджер моделі, щоб pycharm не виділяв те, що для нього неявно
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    tax_code = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        # Забезпечення того, що існує лише один інстанс
        if not self.pk and Company.objects.exists():
            raise ValidationError('There can be only one Company instance.')
        return super(Company, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
