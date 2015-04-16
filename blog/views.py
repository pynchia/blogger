import re
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, \
        TemplateView, FormView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.db.models import Q
from django.contrib.auth.models import User
from . import forms
from .models import Article


class BlogView(ListView):
    # model = Article
    queryset = Article.objects.order_by('-published_on')
    template_name = "blog/blog.html"
    paginate_by = Article.NUM_ARTICLES_IN_PAGE


class AuthorArticlesView(SingleObjectMixin, ListView):
    # model = Article
    template_name = "blog/authorarticles.html"
    paginate_by = Article.NUM_ARTICLES_IN_PAGE

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=User.objects.all())
        return super(AuthorArticlesView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.object.article_set.order_by('-published_on')

    def get_context_data(self, **kwargs):
        context = super(AuthorArticlesView, self).get_context_data(**kwargs)
        context['author'] = self.object
        return context


class SearchArticlesView(ListView):
    # model = Article
    #template_name = "blog/searcharticles.html"
    template_name = "blog/blog.html"
    paginate_by = Article.NUM_ARTICLES_IN_PAGE

    def get_queryset(self):
        oritags = re.findall(r"[\w'-]+",
                             self.request.GET.get(u'search', "").lower())
        # get rid of duplicates
        searchtags = set(oritags)
        queryargs = [Q(tags__contains=" "+i+" ") for i in searchtags]
        return Article.objects.filter(*queryargs).order_by('-published_on')


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


class CreateArticleView(CreateView):
    form_class = forms.ArticleForm
    template_name = "blog/create_updatearticle.html"
    success_url = reverse_lazy("blog:blog")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateArticleView, self).form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    form_class = forms.ArticleForm
    template_name = "blog/create_updatearticle.html"
    success_url = reverse_lazy("blog:blog")

