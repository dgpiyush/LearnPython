# Generated by Django 5.0.3 on 2024-03-24 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]