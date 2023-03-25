from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import *
from core.models import *

# Create your views here.

def categoryblog_list(request):
    category = BlogCategory.objects.all()
    posts = BlogPost.objects.all()
    allmaincategorys = MainCategory.objects.all()
    banks = Bank.objects.all()
    context = {
        'allmain': allmaincategorys,
        'category': category,
        'banks': banks,
        'posts': posts
    }
    return render(request, 'categoryblog_list.html', context)


def categoryblog_detail(request, blogcategory_slug):
    category = get_object_or_404(BlogCategory, slug=blogcategory_slug)
    categorys = BlogCategory.objects.all()
    posts = category.postsblog.all()
    allmaincategorys = MainCategory.objects.all()
    banks = Bank.objects.all()
    context = {
        'allmain': allmaincategorys,
        'category': category,
        'categorys': categorys,
        'banks': banks,
        'posts': posts
    }
    return render(request, 'categoryblog_detail.html', context)


def blogpost_detail(request, blogcategory_slug, postblog_slug):
    category = BlogCategory.objects.all()
    blogpost = get_object_or_404(BlogPost, slug=postblog_slug)
    banks = Bank.objects.all()
    posts = BlogPost.objects.all()
    maincategory = MainCategory.objects.all()
    context = {
        'maincategorys': maincategory,
        'category': category,
        'post': blogpost,
        'banks': banks
    }
    return render(request, 'postblog_detail.html', context)