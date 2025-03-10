from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
#  from django.http import Http404
#  from django.views.decorators.http import require_http_methods
from .models import Article
from .forms import ArticleForm


class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect(reverse('articles_index'))


class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {
            'form': form,
            'article_id': article_id,
            })

    def post(self, request, *args, **kwargs):
        user_can = request.user.has_perm('article.add_article')
        if not user_can:
            return redirect(reverse('articles_index'))
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('articles_index'))
        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/update.html', {
            'form': form,
            'article_id': article_id,
            'user_can': user_can,
            })


class AddArticleView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/create.html', context={
            'user_can': user_can,
            'form': form,
            })

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            article = form.save(commit=False)
            # Дополнительно обрабатываем модель
            # article.content = check_for_spam(form.data['content'])
            article.save()
            return redirect(reverse('articles_index'))

        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/create.html', context={
            'user_can': user_can,
            'form': form,
            })


class IndexView(View):
    def get(self, request, *args, **kwargs):
        # articles = Article.objects.all()[:15]
        articles = Article.objects.order_by('id')[:15]
        # sorted_articles = sorted(list(articles), key='id')
        user_can = request.user.has_perm('article.add_article')
        return render(request, 'articles/index.html', context={
            'articles': articles,
            'user_can': user_can,
            })


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['article_id'])
        return render(request, 'articles/article.html', context={
            'id': article.id,
            'name': article.name,
            'body': article.body,
            })
