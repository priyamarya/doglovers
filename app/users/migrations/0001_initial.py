# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(blank=True, null=True)),
                ('joining_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='related to')),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': ' Users',
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(choices=[('Others', 'Others'), ('Male', 'Male'), ('Female', 'Female')], max_length=125)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='users')),
                ('userlink', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.UserProfile', verbose_name='of user')),
            ],
            options={
                'verbose_name': 'UsersInfo',
                'verbose_name_plural': 'UsersInfo',
            },
        ),
    ]
