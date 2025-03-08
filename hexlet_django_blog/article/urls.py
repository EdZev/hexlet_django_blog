from django.urls import path

# from hexlet_django_blog.article import views
from hexlet_django_blog.article import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='articles_index'),
    path(
        '<int:article_id>/',
        views.ArticleView.as_view(),
        name='article_view',
    ),
    path('create/', views.AddArticleView.as_view(), name='article_create')
]
