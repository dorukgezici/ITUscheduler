# Generated by Django 2.0.1 on 2018-01-03 17:40

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('n_classes', models.PositiveSmallIntegerField(default=1)),
                ('crn', models.PositiveIntegerField(primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=3)),
                ('title', models.CharField(max_length=100)),
                ('instructor', models.CharField(max_length=200)),
                ('building', models.CharField(max_length=20)),
                ('day', models.CharField(max_length=50)),
                ('time_start', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('time_finish', models.CharField(max_length=40, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z'), code='invalid', message='Enter only digits separated by commas.')])),
                ('room', models.CharField(max_length=50)),
                ('capacity', models.PositiveSmallIntegerField()),
                ('enrolled', models.PositiveSmallIntegerField(default=0)),
                ('reservation', models.CharField(max_length=50)),
                ('major_restriction', models.TextField()),
                ('prerequisites', models.TextField()),
                ('class_restriction', models.CharField(max_length=20)),
            ],
            options={
                'get_latest_by': 'crn',
            },
        ),
        migrations.CreateModel(
            name='CourseCode',
            fields=[
                ('refreshed', models.DateTimeField(default=django.utils.timezone.now)),
                ('code', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CourseCode'),
        ),
    ]
