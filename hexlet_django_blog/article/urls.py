from django.urls import path

# from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView


urlpatterns = [
    path('', IndexView.as_view(), name='articles_index'),
    path(
        '<int:article_id>/',
        ArticleView.as_view(),
        name='article_view',
    ),
]
