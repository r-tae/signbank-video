# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-25 06:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import video.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('videofile', models.FileField(storage=video.models.TaggedVideoStorage(), upload_to='video', verbose_name='video file')),
                ('version', models.IntegerField(default=0, verbose_name='Version')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.TaggedVideo')),
            ],
        ),
    ]