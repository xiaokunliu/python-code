# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.PositiveIntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('user_email', models.EmailField(unique=True, max_length=254)),
                ('user_phone', models.CharField(unique=True, max_length=11)),
                ('user_pwd', models.CharField(max_length=32)),
                ('user_really_name', models.CharField(max_length=50, null=True, blank=True)),
                ('user_alias_name', models.CharField(max_length=50, null=True, blank=True)),
                ('user_sex', models.SmallIntegerField(default=1, choices=[(0, b'Male'), (1, b'Female')])),
                ('user_auth', models.CharField(unique=True, max_length=40)),
                ('user_token', models.CharField(unique=True, max_length=40)),
                ('user_token_expires', models.FloatField()),
                ('user_longitude', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('user_latitude', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('user_ip', models.PositiveIntegerField(null=True, blank=True)),
                ('user_label_type', models.CharField(max_length=50, null=True, blank=True)),
                ('user_type', models.SmallIntegerField(default=0, choices=[(0, b'asker'), (1, b'helper')])),
            ],
            options={
                'db_table': 'ss_user',
            },
        ),
        migrations.CreateModel(
            name='UsersAdditional',
            fields=[
                ('ua_id', models.PositiveIntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.PositiveIntegerField(unique=True)),
                ('photo_url', models.URLField(null=True, blank=True)),
                ('domain_desc', models.TextField(null=True, blank=True)),
                ('work_desc', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ss_user_additional',
            },
        ),
    ]
