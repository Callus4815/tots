# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0003_auto_20151006_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default=None, upload_to='item/%Y/%m/%d'),
        ),
    ]
