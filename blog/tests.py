from django.test import TestCase
from .models import Category, Article
# Create your tests here.


class MyTestCase(TestCase):

    fixtures = ['auth.json', 'blog.json', ]

    def setUp(self):
        self.category = Category.objects.get(pk=2)

    def test_articles_of_category(self):
        n = self.category.articles.count()
        self.assertEqual(n, 1)
        self.category.descr="checczo"
        self.category.save()

    def test_categories(self):
        self.assertEqual(self.category.descr, "checczo")

