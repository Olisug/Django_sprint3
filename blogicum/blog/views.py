from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post, Category


POSTS_PER_PAGE: int = 5


def index(request):
    """Открывает главную страницу"""
    posts = Post.objects.select_related('category').filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True).order_by('-pub_date')[:POSTS_PER_PAGE]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)


def post_detail(request, post_id):
    "Открывает детальное описание постов"
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now(),
            pk=post_id))
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    "Открывает описание категории"
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True)
    categories = category.posts.filter(is_published=True,
                                       pub_date__lte=timezone.now())
    template = 'blog/category.html'
    context = {'category': category,
               'post_list': categories}
    return render(request, template, context)
