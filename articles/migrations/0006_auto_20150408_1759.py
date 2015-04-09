# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20150408_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Article Entry', 'verbose_name_plural': 'Article Entries'},
        ),
        migrations.RenameField(
            model_name='opt_images',
            old_name='copt_images',
            new_name='opt_images',
        ),
    ]
