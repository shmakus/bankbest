from django.urls import path
from blog import views

urlpatterns = [
        path('blog/', views.categoryblog_list, name='categoryblog_list'),
        path('blog/<str:blogcategory_slug>', views.categoryblog_detail, name='categoryblog_detail'),
        path('blog/<str:blogcategory_slug>/<str:postblog_slug>', views.blogpost_detail, name='postblog_detail'),

]