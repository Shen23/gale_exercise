# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150407_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='preview',
            field=models.CharField(default=True, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='opt_images',
            name='copt_images',
            field=models.ImageField(upload_to=b''),
        ),
    ]
