from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('articles', views.ArticleViewSet)
router.register('authors', views.AuthorViewSet)


urlpatterns = [
    url(r'^',
        include(router.urls)),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
]
