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
    url(r'^userarticles/$',
        views.AuthorArticlesView.as_view(),
        name='userarticles'),
    url(r'^createarticle/$',
        login_required(views.CreateArticleView.as_view()),
        name='createarticle'),
]
