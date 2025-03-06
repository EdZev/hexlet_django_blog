from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
# from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.http import Http404
from django.views.decorators.http import require_http_methods
from .models import Article
from .forms import AddArticleForm


class AddArticleView(View):
    def post(self, request, *args, **kwargs):
        form = AddArticleForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            form.save()
            return redirect(reverse('articles_index'))
        articles = Article.objects.all()[:15]
        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/index.html', context={
            'articles': articles,
            'user_can': user_can,
            'form': form,
            })


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        form = AddArticleForm()
        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/index.html', context={
            'articles': articles,
            'user_can': user_can,
            'form': form,
            })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'articles/article.html', context={
            'id': article.id,
            'name': article.name,
            'body': article.body,
            })
