from typing import List, Dict

from django.shortcuts import render
from django.http import Http404


def index(request):
    template_name = 'blog/index.html'
    context = {'posts': reversed(posts)}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    if post_id in post_current:
        context = {'post': post_current[post_id]}
        return render(request, template_name, context)
    raise Http404('Нет такой публикации!')


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = {'category_slug': category_slug}
    return render(request, template_name, context)
