from django.conf.urls import include, url
from django.views.defaults import server_error, page_not_found, permission_denied
from django.utils.functional import curry

urlpatterns = [

    url(r'^blog$', 'blog.views.blog'),
    url(r'^portfolio$', 'blog.views.portfolio'),
    url(r'^about$', 'blog.views.about', name='about'),
    url(r'^contact$', 'blog.views.contact'),
    url(r'^category/(?P<category_name>[\w\s]+)$', 'blog.views.category'),
    url(r'^article/(?P<article_id>\d+)$', 'blog.views.page'),
    url(r'^article/(?P<article_id>\d+)/addlike$', 'blog.views.addlike'),
    url(r'^blog/(\d+)/$', 'blog.views.blog'),
    url(r'^portfolio/(\d+)/$', 'blog.views.portfolio'),
    url(r'^category/(?P<category_name>[\w\s]+)/(?P<page_number>\d+)/$', 'blog.views.category'),
    url(r'^$', 'blog.views.index'),
    url(r'^error$',  'blog.views.error'),
    #url(r'^/', 'blog.views.index'),
    #url(r'^', 'blog.views.index'),
   # url(r'^', 'blog.views.index'),

]
