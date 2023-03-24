from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Post, Category, SubCategory, MainCategory, Bank


class MainCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5
    protocol = 'https'


    def items(self):
        return MainCategory.objects.all()


    def lastmod(self, obj):
        return obj.updated_at

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = 'https'

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class SubCategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = 'https'

    def items(self):
        return SubCategory.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

class BankSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.4
    protocol = 'https'

    def items(self):
        return Bank.objects.all()

    def lastmod(self, obj):
        return obj.updated_at