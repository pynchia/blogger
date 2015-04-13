from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, CreateView
from . import forms, models

class BlogView(ListView):
    template_name = "blog/blog.html"
    model = models.Article


class StatsView(TemplateView):
    template_name = "blog/stats.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"


class ContactView(FormView):
    form_class = forms.ContactForm
    template_name = "blog/contact.html"
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        form.send_msg()
        return super(ContactView, self).form_valid(form)


class CreateArticle(CreateView):
    form_class = forms.ArticleForm
    template_name = "blog/createarticle.html"
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateArticle, self).form_valid(form)
