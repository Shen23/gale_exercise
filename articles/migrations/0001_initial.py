# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('category', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to=b'')),
                ('preview', models.CharField(max_length=1000)),
                ('text', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'Article Entry',
                'verbose_name_plural': 'Artries',
            },
        ),
        migrations.CreateModel(
            name='Opt_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opt_images', models.ImageField(upload_to=b'')),
                ('article', models.ForeignKey(related_name='images', to='articles.Article')),
            ],
        ),
    ]
