from django.urls import path
from core import views


handler404 = views.error_page



urlpatterns = [
    path('', views.home, name='home'),

    path('banks/', views.bank_list, name='bank_list'),
    path('<str:maincategory_slug>', views.maincategory_detail, name='maincategory_detail'),
    path('<str:maincategory_slug>/cat/<str:category_slug>/', views.category_detail, name='category_detail'),
    path('<str:category_slug>/post/<str:post_slug>/', views.post_detail, name='post_detail'),
    path('<str:category_slug>/sub/<str:subcategory_slug>/', views.subcategory_detail, name='subcategory_detail'),
    path('banks/<str:bank_slug>/', views.bank_detail, name='bank_detail'),


]
