# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_article_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='test',
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(default=b'', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
    ]
