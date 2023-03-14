from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from blog.models import *
from core.models import *

# Create your views here.

def category_detail(request, category_slug, maincategory_slug):
    category = get_object_or_404(BlogCategory, slug=category_slug)
    allmaincategorys = MainCategory.objects.all()
    maincategorys = get_object_or_404(MainCategory, slug=maincategory_slug, cate__slug=category_slug)
    subcategories = category.subcategories.all()
    posts = category.posts.all()
    banks = Bank.objects.all()
    context = {
        'allmain': allmaincategorys,
        'maincategory': maincategorys,
        'category': category,
        'subcategories': subcategories,
        'posts': posts,
        'banks': banks
    }
    return render(request, 'category_detail.html', context)