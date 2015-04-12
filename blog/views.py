from django.views.generic import ListView, TemplateView, FormView, CreateView
from . import forms

class BlogView(ListView):
    template_name = "blog/blog.html"


class StatsView(TemplateView):
    template_name = "blog/stats.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"


class ContactView(FormView):
    form_class = forms.ContactForm
    template_name = "blog/contact.html"


class CreateArticle(CreateView):
    form_class = forms.ArticleForm
    template_name = "blog/createarticle.html"

