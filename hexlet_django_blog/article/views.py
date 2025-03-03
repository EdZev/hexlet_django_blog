from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Article

# Create your views here.


class ArticlesViews(View):

    def get(self, request, *args, **kwargs):
        # articles = Article.objects.all().map(lambda a: {'id': a.id, 'name': a.name, 'body': a.body})
        articles = Article.objects.all()
        print(articles)
        return render(
            request,
            'articles/index.html',
            context={'articles': articles}
        )


def get_tags_and_id(request, article_id):
    '''try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404()'''
    article = get_object_or_404(Article, pk=article_id)
    return render(
        request,
        'articles/article.html',
        context={
            'id': article.id,
            'name': article.name,
            'body': article.body,
            },
        )
