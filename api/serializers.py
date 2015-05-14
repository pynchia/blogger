from rest_framework import serializers
from django.contrib.auth.models import User
from blog import models


class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True,
                            queryset=models.Article.objects.all())

    class Meta:
        model = models.Category


class CategoryListSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Category
        fields = ('url', 'id', 'name', )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Article


class ArticleListSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source='get_absolute_url', read_only=True)

    class Meta:
        model = models.Article
        fields = ('url', 'id', 'title', )


class AuthorSerializer(serializers.ModelSerializer):
    articles = serializers.PrimaryKeyRelatedField(many=True,
                            queryset=models.Article.objects.all())

    class Meta:
        model = User
        # WIP fields = (
        exclude = ('password', )
