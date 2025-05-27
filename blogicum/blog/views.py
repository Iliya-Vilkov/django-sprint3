from datetime import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post

def get_post(request):
    


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )[:5]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post,
                             pub_date__lte=datetime.now(),
                             is_published=True,
                             category__is_published=True,
                             id=post_id)
    context = {'post': post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    ).filter(category=category)
    context = {'category': category,
               'post_list': post_list}
    return render(request, template_name, context)
