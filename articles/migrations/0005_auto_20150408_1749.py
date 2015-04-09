# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150408_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview',
            field=models.CharField(max_length=1000),
        ),
    ]
