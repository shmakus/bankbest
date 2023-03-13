from django.shortcuts import render, get_object_or_404
from core.models import MainCategory, Category, SubCategory, Post, Bank, RatingForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import View
# Create your views here.

class ESearchView(View):
    template_name = 'search/index.html'

    def get(self, request, *args, **kwargs):
        context = {}

        question = request.GET.get('q')
        if question is not None:
            search_articles = Post.objects.filter(name__search=question)

            # формируем строку URL, которая будет содержать последний запрос
            # Это важно для корректной работы пагинации
            context['last_question'] = '?q=%s' % question

            current_page = Paginator(search_articles, 10)

            page = request.GET.get('page')
            try:
                context['article_lists'] = current_page.page(page)
            except PageNotAnInteger:
                context['article_lists'] = current_page.page(1)
            except EmptyPage:
                context['article_lists'] = current_page.page(current_page.num_pages)

                return render(template_name = self.template_name, context=context)