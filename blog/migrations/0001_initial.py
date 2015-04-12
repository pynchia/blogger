# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(help_text=b'a concise but useful title', max_length=128)),
                ('body', models.TextField(help_text=b'the content of the article')),
                ('tags', models.CharField(help_text=b'separate tags with space', max_length=128, blank=True)),
                ('image', models.ImageField(help_text=b'preferred size is 256 by 160', upload_to=b'articleimg')),
                ('author', models.ForeignKey(editable=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('descr', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(help_text=b'pick as many as necess', to='blog.Category'),
        ),
    ]
