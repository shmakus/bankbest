from django.contrib import admin
from .models import *
from blog.models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
# Register your models here.


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class BankAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Bank
        fields = '__all__'


class CategoryAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = Category
        fields = '__all__'

class MainCategoryAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = MainCategory
        fields = '__all__'

class SubCategoryAdminForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=CKEditorUploadingWidget())
    class Meta:
        model = SubCategory
        fields = '__all__'


@admin.register(MainCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}
    form = MainCategoryAdminForm

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'maincategory')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}
    form = CategoryAdminForm


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'category')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}
    form = SubCategoryAdminForm

class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ('email', 'name')
    save_on_top = True


class BankAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}
    form = BankAdminForm


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'maincategory', 'category', 'bank', 'slug', 'link')
    list_display_links = ('id', 'name')
    list_filter = ('category', 'bank')
    search_fields = ('name', 'category__name')
    prepopulated_fields = {'slug': ("name",)}
    form = PostAdminForm

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
