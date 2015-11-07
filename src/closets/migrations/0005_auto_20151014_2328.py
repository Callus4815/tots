# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0004_auto_20151008_0007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(upload_to='item/%Y/%m/%d', null=True, blank=True),
        ),
    ]
