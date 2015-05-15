from rest_framework import serializers
from django.contrib.auth.models import User
from blog import models


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='article-detail',
                                                   read_only=True)

    class Meta:
        model = models.Category


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Category
        fields = ('url', 'name', )


class ArticleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Article


class ArticleListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Article
        fields = ('url', 'title', )


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    articles = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='article-detail',
                                                   read_only=True)

    class Meta:
        model = User
        exclude = ('password', )


class AuthorListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username')

