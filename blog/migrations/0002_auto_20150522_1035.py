# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'category',
                'verbose_name': '\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '\u0421\u0442\u0430\u0442\u044c\u044f', 'verbose_name_plural': '\u0441\u0442\u0430\u0442\u044c\u0438'},
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': '\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', 'verbose_name_plural': '\u043a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0438'},
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_user',
            field=models.ForeignKey(default=b'', verbose_name=b'\xd0\x90\xd0\xb2\xd1\x82\xd0\xbe\xd1\x80', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.TextField(default=b''),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_title',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comments_text',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438'),
        ),
    ]
