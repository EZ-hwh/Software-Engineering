# Generated by Django 2.2.3 on 2020-05-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20200411_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='message',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='register',
            name='password',
        ),
        migrations.RemoveField(
            model_name='register',
            name='register_id',
        ),
        migrations.RemoveField(
            model_name='register',
            name='username',
        ),
        migrations.AddField(
            model_name='todolist',
            name='name',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='checksum',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]