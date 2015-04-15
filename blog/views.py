from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.views.generic.detail import SingleObjectMixin
from . import forms, models


class BlogView(ListView):
    template_name = "blog/blog.html"
    model = models.Article
    queryset = models.Article.objects.order_by('-published_on')
    paginate_by = models.Article.NUM_ARTICLES_IN_PAGE


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


class AuthorArticlesView(SingleObjectMixin, ListView):
    template_name = "blog/userarticles.html"


class CreateArticleView(CreateView):
    form_class = forms.ArticleForm
    template_name = "blog/createarticle.html"
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateArticleView, self).form_valid(form)
