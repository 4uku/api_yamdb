# Generated by Django 2.2.16 on 2021-10-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20211008_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(blank=True, max_length=300, verbose_name='Биография'),
        ),
    ]
