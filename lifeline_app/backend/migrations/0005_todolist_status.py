# Generated by Django 3.0.3 on 2020-05-16 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_register_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
