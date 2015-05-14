from rest_framework import viewsets
from blog import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """
    this viewset provides 'list' and 'retrieve' actions to everyone.
    'create', 'update' and 'destroy' actions to admins.
    The 'list' action allows searching for a substring (case ins.)
    of its name via the 'name' url param (/api/categories/?name=<substring>)
    """
    pass


class ArticleViewSet(viewsets.ModelViewSet):
    """
    this viewset provides 'list' and 'retrieve' actions to everyone.
    'create', 'update' and 'destroy' actions to authors (article owners) only.
    The 'list' action allows searching for a substring (case ins.)
    of its title via the 'title' url param (/api/articles/?title=<substring>)
    """
    pass


