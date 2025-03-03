from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ['name', 'body']
    list_filter = (('created_at', DateFieldListFilter),)


# admin.site.register(Article, ArticleAdmin)

# Register your models here.
