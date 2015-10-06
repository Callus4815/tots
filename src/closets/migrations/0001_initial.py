# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('condition', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=140)),
                ('posted_at', models.DateTimeField()),
                ('favorited_items', models.ManyToManyField(related_name='favorited_items', to=settings.AUTH_USER_MODEL, through='closets.Favorite')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='favorite',
            name='item',
            field=models.ForeignKey(to='closets.Item'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
