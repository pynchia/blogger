from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    url(r'^$',
        views.BlogView.as_view(),
        name='blog'),
    url(r'^stats/$',
        views.StatsView.as_view(),
        name='stats'),
    url(r'^about/$',
        views.AboutView.as_view(),
        name='about'),
    url(r'^contact/$',
        views.ContactView.as_view(),
        name='contact'),
    url(r'^authorarticles/(?P<pk>\d+)/$',
        views.AuthorArticlesView.as_view(),
        name='authorarticles'),
    url(r'^createarticle/$',
        login_required(views.CreateArticleView.as_view()),
        name='createarticle'),
    url(r'^updatearticle/(?P<pk>\d+)/$',
        login_required(views.UpdateArticleView.as_view()),
        name='updatearticle'),
    url(r'^search/$',
        views.SearchArticlesView.as_view(),
        name='search'),
]
