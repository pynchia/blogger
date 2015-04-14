from django import forms
from django.core.mail import EmailMessage
import re
from . import models
from django.conf import settings


class ContactForm(forms.Form):
    required_css_class = 'required'

    name = forms.CharField(required=True, max_length=64)
    email_address = forms.EmailField(required=True, max_length=128)
    message = forms.CharField(required=True, widget=forms.Textarea)

    def send_msg(self):
        from_email = self.cleaned_data['email_address']
        email = EmailMessage(subject='Msg from Blog',
                             cc=[from_email, ],
                             body=self.cleaned_data['message'],
                             to=[settings.EMAIL_HOST_USER, ],
                             headers={'Reply-To': from_email})
        email.send()


class ArticleForm(forms.ModelForm):
    required_css_class = 'required'

    class Meta:
        model = models.Article
        fields = ['title', 'body', 'categories', 'tags', 'image']

    def clean_tags(self):
        return " ".join(set(re.findall(r"[\w'-]+",
                                       self.cleaned_data['tags']))).lower()

    def clean(self):
        tags = self.cleaned_data.get('tags')
        categs = self.cleaned_data.get('categories')
        if tags and categs:
            categs = [c.name.lower() for c in categs]
            tags += " "+" ".join(t for t in categs if t not in tags)
            self.cleaned_data['tags'] = tags

