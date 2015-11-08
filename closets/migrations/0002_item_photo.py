# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.FileField(default=None, upload_to='item/%Y/%m/%d'),
        ),
    ]
