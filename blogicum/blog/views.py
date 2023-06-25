from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post, Category


def index(request):
    "Открывает главную страницу - Лента записей"
    template = 'blog/index.html'
    posts = (
        Post.objects.filter(
            is_published=True,
            pub_date_lte=timezone.now(),
            category__is_published=True)
        .order_by('-id')
    )
    context = {'posts': posts}
    return render(request, template, context)


def post_detail(request, post_id):
    "Открывает детальное описание постов"
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.filter(
            is_published=True,
            category__is_published=True,
            pub_date_lte=timezone.now(),
            pk=post_id)
            )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    "Открывает описание категории"
    template = 'blog/category.html'
    category = get_object_or_404(Category,
                                 slug=category_slug,
                                 is_published=True)
    category_posts = Post.objects.select_related('author',
                                                 'location',
                                                 'category')
    context = {'category': category,
               'post': category_posts}
    return render(request, template, context)
