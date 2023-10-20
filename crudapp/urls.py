from django.urls import path

from crudapp.views import article_func, article_detail, article_create, article_edit, article_delete

urlpatterns = [
    path('',article_func, name="article_func"),   
    path('<slug>', article_detail, name='article_detail'),
    path('article_create/', article_create, name='article_create'),
    path('<slug>/edit', article_edit, name='article_edit'),
    path('<slug>/delate', article_delete, name='article_delete')
]