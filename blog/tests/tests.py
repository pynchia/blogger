from django.test import TestCase
from django.core.urlresolvers import reverse
from blog.models import Category, Article
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
        self.author = Category.objects.get(pk=1)

    def test_relat_between_articles_and_categories(self):
        n = self.catmusic.articles.count()
        self.assertEqual(n, 2)
        n = self.catphoto.articles.count()
        self.assertEqual(n, 1)

    def test_homepage_redirect_to_blog(self):
        response = self.client.get(reverse('home'))
        # it should be redirected permanently HTTP 301
        self.assertRedirects(response, reverse('blog:blog'), status_code=301)

    def test_get_blog_page(self):
        response = self.client.get(reverse('blog:blog'))
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        return response

    def test_articles_on_blogpage(self):
        response = self.test_get_blog_page()
        # there should be three articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 3)
        # and there should be three categories on the page
        numcat = len(response.context['categories'])
        self.assertEqual(numcat, 3)

    def test_categ_has_articles(self):
        response = self.client.get(reverse('blog:categarticles',
                                           kwargs={'pk': self.catmusic.id, })
                                  )
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        # there should be two articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 2)

    def test_author_has_articles(self):
        response = self.client.get(reverse('blog:authorarticles',
                                           kwargs={'pk': self.author.id, })
                                  )
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        # there should be one article on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 1)

    def test_createnewarticle(self):
        logged = self.client.login(username='pinom', password='xyzxyz')
        self.assertTrue(logged)
        ARTICLE_TITLE = "Post test"
        with open('blog/tests/img_ok-horiz.jpg') as imgf:
            post_data = {'title': ARTICLE_TITLE,
                         'body': """This is a test.
                                    The sun is hot and the earth is round""",
                         'categories': ('1', '2'),
                         'tags': "cippa",
                         'image': imgf}
            response = self.client.post(reverse('blog:createarticle'),
                                        data=post_data)
        # it should be redirected temp. HTTP 302
        self.assertRedirects(response, reverse('blog:blog'), status_code=302)
        # get the blog page
        response = self.test_get_blog_page()
        # now there should be four articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 4)
        # and the first(latest) article must be the one we created
        latestart = response.context['object_list'][0]
        self.assertEqual(latestart.title, ARTICLE_TITLE)
