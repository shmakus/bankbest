from django.shortcuts import render, get_object_or_404
from .models import MainCategory, Category, SubCategory, Post, Bank, RatingForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View

def home(request):
    maincategorys = MainCategory.objects.all()
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    posts = Post.objects.all()
    banks = Bank.objects.all()
    context = {
        'maincategorys': maincategorys,
        'categories': categories,
        'subcategories': subcategories,
        'posts': posts,
        'banks': banks,
        'star_form': RatingForm
    }
    return render(request, 'home.html', context)


def maincategory_detail(request, maincategory_slug):
    maincategorys = get_object_or_404(MainCategory, slug=maincategory_slug)
    category = maincategorys.cate.all()
    maincategory = MainCategory.objects.all()
    posts = maincategorys.maincate.all()
    banks = Bank.objects.all()


    context = {
        'maincategory': maincategory,
        'maincategorys': maincategorys,
        'category': category,
        'posts': posts,
        'banks': banks

    }
    return render(request, 'maincategory_detail.html', context)


def category_detail(request, category_slug, maincategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
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


def post_detail(request, category_slug, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'post': post,
    }
    return render(request, 'post_detail.html', context)


def subcategory_detail(request, category_slug, subcategory_slug):
    category = get_object_or_404(Category, slug=category_slug)
    subcategory = get_object_or_404(SubCategory, slug=subcategory_slug, category__slug=category_slug)
    posts = subcategory.posts.all()
    subcategories = category.subcategories.all()
    maincategory = MainCategory.objects.all()
    banks = Bank.objects.all()
    context = {
        'subcategories': subcategories,
        'subcategory': subcategory,
        'posts': posts,
        'maincategorys': maincategory,
        'banks': banks
    }
    return render(request, 'subcategory_detail.html', context)


def bank_detail(request, bank_slug):
    maincategory = MainCategory.objects.all()
    banks = Bank.objects.all()
    bank = get_object_or_404(Bank, slug=bank_slug)
    posts = bank.posts.all()
    context = {
        'bank': bank,
        'banks': banks,
        'posts': posts,
        'maincategory': maincategory
    }
    return render(request, 'bank_detail.html', context)


def bank_list(request):
    bank = Bank.objects.all()
    maincategorys = MainCategory.objects.all()
    context = {
        'bank': bank,
        'maincategorys': maincategorys
    }
    return render(request, 'bank_list.html', context)



