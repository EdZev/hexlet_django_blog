from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Article


class AddArticleForm(forms.ModelForm):
    # name = forms.CharField(label='Название', max_length=200)
    # body = forms.CharField()
    class Meta:
        model = Article
        fields = ['name', 'body']
        labels = {
            'name': _('Название'),
            'body': _('Текст'),
        }
        help_texts = {
            'name': _('Название статьи'),
            'body': _('Какой-то текст'),
        }
        widgets = {
              'name': forms.TextInput(
                  attrs={
                      'class': 'some-class',
                      'placeholder': 'Название статьи'
                      }),
              'body': forms.Textarea(
                  attrs={
                      'class': 'some-class',
                      'placeholder': 'Текст статьи'
                      }),
          }
