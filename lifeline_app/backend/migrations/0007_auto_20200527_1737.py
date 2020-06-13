# Generated by Django 3.0.3 on 2020-05-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200516_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='account',
            name='privilege',
        ),
        migrations.AddField(
            model_name='account',
            name='addr',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='elearning_login',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='elearning_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='elearning_password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='picture',
            field=models.CharField(default='/static/img/user0.png', max_length=50),
        ),
    ]