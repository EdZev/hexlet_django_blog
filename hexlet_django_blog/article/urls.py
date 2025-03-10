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
    path('create/', views.AddArticleView.as_view(), name='article_create'),
    path(
        '<int:id>/edit/',
        views.ArticleFormEditView.as_view(),
        name='articles_update'),
    path(
        '<int:id>/delete/',
        views.ArticleFormDeleteView.as_view(),
        name='articles_delete'),
]
