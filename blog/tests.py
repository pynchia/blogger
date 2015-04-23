from django.test import TestCase
from django.core.urlresolvers import reverse
from .models import Category, Article
# Create your tests here.


class MyTestCase(TestCase):

    fixtures = ['auth.json', 'blog.json', ]

    @classmethod
    def setUpTestData(cls):
        # setup the data for the testcase. The right
        # place where to populate the db with records
        # Still fresh to every test method called
        # but it's much quicker/lighter on the DB
        # than doing it in the setUp method, which
        # can be used to setup instance variables
        # and avoid repeating code 
        pass

    def setUp(self):
        self.catmusic = Category.objects.get(pk=1)
        self.catphoto = Category.objects.get(pk=2)

    def test_relat_between_articles_and_categories(self):
        n = self.catmusic.articles.count()
        self.assertEqual(n, 2)
        n = self.catphoto.articles.count()
        self.assertEqual(n, 1)

    def test_homepage_redirect_to_blog(self):
        response = self.client.get(reverse('home'))
        self.assertRedirects(response, reverse('blog:blog'), status_code=301)

    def test_blog_page_has_three_articles(self):
        response = self.client.get(reverse('blog:blog'))
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        # there should be three articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 3)

    def test_music_categ_has_two_articles(self):
        response = self.client.get(reverse('blog:categarticles',
                                           kwargs={'pk': self.catmusic.id, })
                                  )
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        # there should be two articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 2)
