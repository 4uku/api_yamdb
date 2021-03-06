# Generated by Django 2.2.16 on 2021-10-15 13:00

import django.core.validators
from django.db import migrations, models
import reviews.validators


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0029_merge_20211015_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='genre',
            field=models.ManyToManyField(blank=True, related_name='genre_title', to='reviews.Genre'),
        ),
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1200), reviews.validators.MaxYearValidator()]),
        ),
    ]
