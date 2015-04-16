from django import forms
from django.core.mail import EmailMessage
import re
from django.conf import settings
from . import models
#from blogger.utils import xyz


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

    # def clean_tags(self):
    #     return " ".join(set(re.findall(r"[\w'-]+",
    #                                    self.cleaned_data['tags']))).lower()

    def clean(self):
        tags = re.findall(r"[\w'-]+", self.cleaned_data['tags'])
        categs = self.cleaned_data.get('categories')
        # if the categs are valid (i.e. at least one selected)
        if categs:
            categs = [c.name.lower() for c in categs]
            # now add categs to tags and remove duplicates
            newtags = set(tags+categs)
            # rejoin the tags and add a space on both ends to enable
            # exact search of tags
            self.cleaned_data['tags'] = " "+" ".join(newtags)+" "

