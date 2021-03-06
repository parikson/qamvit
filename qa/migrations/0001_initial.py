# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-22 10:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=1000)),
                ('likes', models.IntegerField(default=0)),
                ('written_by', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date(2017, 11, 22))),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=50)),
                ('content', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionfield', models.CharField(max_length=200)),
                ('no_of_answers', models.IntegerField(default=0)),
                ('date', models.DateField(default=datetime.date(2017, 11, 22))),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('tag_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=50)),
                ('no_of_questions', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Userdetails',
            fields=[
                ('USN', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('semester', models.IntegerField(max_length=1)),
                ('name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=20)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='question_tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='qa.Tags'),
        ),
        migrations.AddField(
            model_name='questions',
            name='user_usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Userdetails'),
        ),
        migrations.AddField(
            model_name='like',
            name='liked_user_usn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Userdetails'),
        ),
        migrations.AddField(
            model_name='blog',
            name='user_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Userdetails'),
        ),
        migrations.AddField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.Questions'),
        ),
    ]
