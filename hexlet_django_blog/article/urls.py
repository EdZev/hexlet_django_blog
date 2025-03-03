from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import ArticlesViews

urlpatterns = [
    path('', ArticlesViews.as_view(), name='articles_index'),
    path(
        '<int:article_id>/',
        views.get_tags_and_id,
        name='article',
    ),
]
