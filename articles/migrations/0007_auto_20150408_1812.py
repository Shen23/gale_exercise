# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20150408_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Article Entry', 'verbose_name_plural': 'Artries'},
        ),
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
