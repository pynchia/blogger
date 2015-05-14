from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from blog import models
from . import serializers
from .permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    """
    this viewset provides 'list' and 'retrieve' actions to everyone.
    'create', 'update' and 'destroy' actions to admins only.
    The 'list' action allows searching for a substring (case ins.)
    of its name via the 'name' url param (/api/categories/?name=<substring>)
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsAdminOrReadOnly,
                         )
    queryset = models.Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CategoryListSerializer
        return serializers.CategorySerializer

    def get_queryset(self):
        substring = self.request.QUERY_PARAMS.get('name', None)
        if substring is not None:
            return self.queryset.filter(name__contains=substring.lower())
        return self.queryset


class ArticleViewSet(viewsets.ModelViewSet):
    """
    this viewset provides 'list' and 'retrieve' actions to everyone.
    'create', 'update' and 'destroy' actions to authors (owners) only.
    The 'list' action allows searching for a substring (case ins.)
    of its title via the 'title' url param (/api/articles/?title=<substring>)
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, 
                          IsAuthorOrReadOnly,
                         )
    queryset = models.Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.ArticleListSerializer
        else:
            return serializers.ArticleSerializer

    def get_queryset(self):
        substring = self.request.QUERY_PARAMS.get('title', None)
        if substring is not None:
            return self.queryset.filter(title__contains=substring.lower())
        return self.queryset


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    this viewset provides 'list' and 'retrieve' actions to everyone.
    """
    serializer_class = serializers.AuthorSerializer
    queryset = User.objects.all()
