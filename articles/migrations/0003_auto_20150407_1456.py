# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20150406_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b'media'),
        ),
        migrations.AlterField(
            model_name='opt_images',
            name='copt_images',
            field=models.ImageField(upload_to=b'media'),
        ),
    ]
