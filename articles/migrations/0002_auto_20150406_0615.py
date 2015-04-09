# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opt_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copt_images', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=True, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opt_images',
            name='article',
            field=models.ForeignKey(related_name='images', to='articles.Article'),
        ),
    ]
