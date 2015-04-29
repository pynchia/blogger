import re
from PIL import Image
from django import forms
from django.core.mail import EmailMessage
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from .models import Article


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
        model = Article
        fields = ['title', 'body', 'categories', 'tags', 'image']

    # def clean_tags(self):
    #     return " ".join(set(re.findall(r"[\w'-]+",
    #                                    self.cleaned_data['tags']))).lower()

    def clean_image(self):
        imgdata = self.cleaned_data.get('image')
        # if it's there it's valid
        if imgdata:
            if imgdata.size > settings.MAX_UPLOAD_SIZE:
                raise forms.ValidationError(
                        _('The image file size must be under %(max_size)d bytes. Current file size is %(cur_size)d bytes.'),
                        code='invalid',
                        params={'max_size': settings.MAX_UPLOAD_SIZE,
                                'cur_size': imgdata.size })
        return imgdata

    def clean(self):
        super(ArticleForm, self).clean()
        tags = re.findall(r"[\w'-]+", self.cleaned_data['tags'])
        categs = self.cleaned_data.get('categories')
        # if the categs are valid (i.e. at least one selected)
        if categs:
            categs = [c.name.lower() for c in categs]
            # add the selected categs to the tags and remove duplicates
            newtags = set(tags+categs)
            # rejoin the tags and add a space on both ends to enable
            # exact searching of tags
            self.cleaned_data['tags'] = " "+" ".join(newtags)+" "

    def save(self, *args, **kwargs):
        article = super(ArticleForm, self).save(*args, **kwargs)
        if 'image' in self.changed_data:
            im = Image.open(article.image.path)
            im.thumbnail((Article.IMG_MAX_WIDTH,
                          Article.IMG_MAX_HEIGHT,), Image.ANTIALIAS)
            im.save(article.image.path)
        return article

