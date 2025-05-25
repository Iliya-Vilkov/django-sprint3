from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category_is_published=True,
        pub_date__lte=datetime.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    context = get_object_or_404((
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category_is_published=True,
        pub_date__lte=datetime.now()
    ), post_id=id)
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    context = {'category': category,
               'post_list': (
                   'category',
                   'location',
                   'author'
               ).filter(
                   is_published=True,
                   category_is_published=True,
                   pub_date__lte=datetime.now()
               ).filter(category=category)}
    return render(request, template_name, context)
