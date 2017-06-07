# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20150909_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'Name')),
                ('phone', models.CharField(max_length=300, verbose_name=b'Phone')),
                ('date', models.DateField(auto_now_add=True, verbose_name=b'Date')),
                ('product', models.ForeignKey(verbose_name=b'product', to='blog.Article')),
            ],
        ),
    ]
