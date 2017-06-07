from django.contrib import admin
from django.contrib.auth.models import *
from blog.models import Article, Comments, Category, Order


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 2

class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_text', 'article_date', 'article_category',
              'article_user', 'article_image']
    list_filter = ['article_date']
    #inlines = [ArticleInline]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comments_text']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'name', 'phone', 'date']
    ordering = ['product']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Order, OrderAdmin)
#admin.site.register(Comments, CommentsAdmin)

admin.site.unregister(User)
admin.site.unregister(Group)


