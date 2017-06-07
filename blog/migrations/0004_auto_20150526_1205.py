# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150522_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_image',
            field=models.ImageField(default=b'', upload_to=b'/img/category/', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e \xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_date',
            field=models.DateTimeField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd1\x83\xd0\xb1\xd0\xbb\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=b'', upload_to=b'/img/article/', verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8c\xd1\x8e \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(default=b'', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_article',
            field=models.ForeignKey(verbose_name=b'\xd0\x94\xd0\xbb\xd1\x8f \xd0\xba\xd0\xb0\xd0\xba\xd0\xbe\xd0\xb9 \xd1\x81\xd1\x82\xd0\xb0\xd1\x82\xd1\x8c\xd0\xb8', to='blog.Article'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(default=b'', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82'),
        ),
    ]
