# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150909_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='test',
            field=ckeditor.fields.RichTextField(default=0),
            preserve_default=False,
        ),
    ]
