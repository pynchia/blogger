# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(help_text=b'the content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(help_text=b'as many as necessary', related_name='articles', to='blog.Category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(help_text=b'optimal size 256x160 pixels', upload_to=b'articleimg'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.CharField(help_text=b'space or comma separated', max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(help_text=b'concise but useful', max_length=128),
        ),
    ]
