from django import forms
from . import models


class ContactForm(forms.Form):
    required_css_class = 'required'

    name = forms.CharField(required=True, max_length=64)
    email_address = forms.EmailField(required=True, max_length=128)
    message = forms.CharField(required=True, widget=forms.Textarea)


class ArticleForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'categories', 'tags', 'image']


