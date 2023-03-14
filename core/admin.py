from django.contrib import admin
from .models import *
from blog.models import *
# Register your models here.



@admin.register(MainCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'maincategory')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('email', 'name')
    save_on_top = True


class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'maincategory', 'category', 'bank', 'slug', 'link')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'bank')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ("name",)}


class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('id', 'value')
    list_display_links = ('id', 'value')


class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'star', 'post')
    list_display_links = ('id', 'star', 'post')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'text', 'parent', 'post')
    list_display_links = ('id', 'email', 'name', 'text', 'parent', 'post')
    readonly_fields = ('name', 'email')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

admin.site.register(Bank, BankAdmin)
admin.site.register(RatingStar, RatingStarAdmin)
admin.site.register(Rating, RatingAdmin)
