from django.shortcuts import render, get_object_or_404
from core.models import MainCategory, Category, SubCategory, Post, Bank, RatingForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
# Create your views here.

from django.shortcuts import render
from core.models import Post
from search.forms import SearchForm


def search(request):
    query = request.GET.get('query')
    if query:
        results = Post.objects.filter(name__icontains=query)
        maincategorys = MainCategory.objects.all()
        categories = Category.objects.all()
        subcategories = SubCategory.objects.all()
        posts = Post.objects.all()
        banks = Bank.objects.all()

        context = {
            'query': query,
            'results': results,
            'maincategorys': maincategorys,
            'categories': categories,
            'subcategories': subcategories,
            'posts': posts,
            'banks': banks,
            'star_form': RatingForm
        }
        return render(request, 'search_results.html', context)
    return render(request, 'base.html')