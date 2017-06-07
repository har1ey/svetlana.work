#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
#from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'категории'

    category_name = models.CharField(max_length=50, verbose_name='Имя категории транслитом')
    category_title = models.CharField(default='', max_length=50, verbose_name='Название категории')
    category_image = models.ImageField(default='', upload_to='img/category/', verbose_name='Превью категории')

    def __unicode__(self):
        return self.category_title


class Article(models.Model):
    class Meta:
        db_table = 'article'
        verbose_name = 'Статья'
        verbose_name_plural = 'статьи'

    article_title = models.CharField(max_length=250, verbose_name='Название статьи')
    article_text = RichTextUploadingField()
    article_category = models.ManyToManyField(Category, verbose_name=u"Категории")
    article_date = models.DateTimeField(verbose_name='Дата публикации')
    article_likes = models.IntegerField(default=0)
    article_image = models.ImageField(default='', upload_to='img/article/', verbose_name='Превью статьи')
    article_user = models.ForeignKey(User, default='', verbose_name='Автор')

    def __unicode__(self):
        return self.article_title


class Comments(models.Model):
    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'комментарии'

    comments_text = models.TextField(default='', verbose_name='Текст')
    comments_article = models.ForeignKey(Article, verbose_name='Для какой статьи')

class Order(models.Model):
    product = models.ForeignKey(Article, verbose_name="product")
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=300, verbose_name='Телефон')
    date = models.DateField("Date", auto_now_add=True)
