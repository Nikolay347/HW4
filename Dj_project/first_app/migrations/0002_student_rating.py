# Generated by Django 5.2 on 2025-05-07 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='rating',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
