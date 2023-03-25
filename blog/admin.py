from django.contrib import admin
from blog.models import BlogCategory, BlogPost
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())
    class Meta:
        model = BlogPost
        fields = '__all__'

@admin.register(BlogCategory)
class CategoryBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}


@admin.register(BlogPost)
class PostBlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ("name",)}
    form = PostAdminForm





# Register your models here.
