# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0005_auto_20151014_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(default=datetime.datetime(2015, 11, 8, 14, 32, 11, 830924, tzinfo=utc), upload_to='item/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
