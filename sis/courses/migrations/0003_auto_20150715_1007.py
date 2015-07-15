# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20150715_0955'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('discription', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('discription', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('discription', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('discription', models.CharField(max_length=128)),
                ('course', models.ForeignKey(to='courses.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('code', models.CharField(unique=True, max_length=128)),
                ('discription', models.CharField(max_length=128)),
                ('module', models.ForeignKey(to='courses.Module')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='topic',
            field=models.ForeignKey(to='courses.Topic'),
        ),
        migrations.AddField(
            model_name='activity',
            name='activity',
            field=models.ForeignKey(to='courses.Lesson'),
        ),
    ]
