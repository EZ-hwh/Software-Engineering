# Generated by Django 2.2.3 on 2020-04-11 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scheduler',
            name='time',
        ),
        migrations.AlterField(
            model_name='board',
            name='board_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='homework',
            name='homework_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='register',
            name='register_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='scheduler_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='timezone',
            name='timezone_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='todolist_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('time_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_time', models.CharField(default='0-0', max_length=10)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Course')),
                ('scheduler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Scheduler')),
            ],
        ),
    ]
