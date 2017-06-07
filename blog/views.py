#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import *
from blog.forms import ArticleForm, OrderForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from handmade import settings
# Create your views here.


def index(request):
    args = {}

    article_likes = Article.objects.all().order_by('-article_likes')[0:6]
    args['article_likes'] = article_likes

    article_last = Article.objects.all().order_by('-article_date')[0:3]
    args['article_last'] = article_last

    cat = Category.objects.all()
    args['category'] = cat

    return render_to_response('index.html', args, context_instance=RequestContext(request))


def category(request, category_name, page_number=1):
    args = {}

    cat = Category.objects.get(category_name=category_name)
    args['category'] = cat

    articles = Article.objects.filter(article_category=cat)

    paginator = Paginator(articles, 6)

    articles = paginator.page(page_number)

    args['articles'] = articles

    art_count = Article.objects.filter(article_category=cat).count()
    args['art_count'] = art_count

    return render_to_response('category.html', args, context_instance=RequestContext(request))


def blog(request, page_number=1):

    args = {}

    articles = Article.objects.all().order_by('-article_date')

    paginator = Paginator(articles, 3)

    articles = paginator.page(page_number)

    args['articles'] = articles

    cat = Category.objects.all()
    args['category'] = cat

    return render_to_response('blog.html', args, context_instance=RequestContext(request))


def portfolio(request, page_number=1):
    args = {}

    cat = Category.objects.all()

    paginator = Paginator(cat, 9)

    cat = paginator.page(page_number)

    cat_count = Category.objects.all().count()

    args['category'] = cat
    args['category_count'] = cat_count

    return render_to_response('portfolio.html', args, context_instance=RequestContext(request))


def page(request, article_id):
    args = {}

    article = Article.objects.get(id=article_id)
    args['article'] = article
    #args['text']= article.article_text

    cat = Category.objects.all()
    args['category'] = cat

    form = OrderForm(request.POST or None, initial={"product": article})

    if request.method == "POST":
        if form.is_valid():
            form.save()

            email_subject = ' Message in svetlana.work '
            email_body = "New request!\n\n" \
                         "Name: %s \n" \
                         "Phone: %s \n" \
                         "Product: %s \n" \
                          % (form.cleaned_data['name'], form.cleaned_data['phone'], form.cleaned_data['product'])
            send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, ['nik.vakhrushev@gmail.com'])

            return HttpResponseRedirect("{}?sended=True".format('/article/%s' % article_id))

    args['sended'] = request.GET.get('sended', False)

    return render_to_response('page.html', args, context_instance=RequestContext(request, {'form': form, }))


def addlike(request, article_id):
    if article_id in request.COOKIES:
        return HttpResponseRedirect('/article/%s' % article_id)
    else:
        article = Article.objects.get(id=article_id)
        article.article_likes += 1
        article.save()
        response = HttpResponseRedirect('/article/%s' % article_id)
        response.set_cookie(article_id, "svetlana.work")
        return response


def about(request):

    args = {}

    cat = Category.objects.all()
    args['category'] = cat

    return render_to_response('about.html', args, context_instance=RequestContext(request))


def contact(request):

    return render_to_response('contact.html', context_instance=RequestContext(request))


def err500(request):

    return HttpResponseRedirect('/error')

def err404(request):

    return HttpResponseRedirect('/error')

def error(request):
    args = {}

    cat = Category.objects.all()
    args['category'] = cat

    return render_to_response('error.html', args, context_instance=RequestContext(request))
