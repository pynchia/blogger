from django.test import TestCase
from django.core import mail
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
        # and avoid repeating code  instead
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

    def test_homepage_redirects_to_blog(self):
        response = self.client.get(reverse('home'))
        # it should be redirected permanently HTTP 301
        self.assertRedirects(response, reverse('blog:blog'), status_code=301)

    def get_page_200(self, pagename, kwargs=None):
        response = self.client.get(reverse(pagename, kwargs=kwargs))
        # the page exists and is returned
        self.assertEqual(response.status_code, 200)
        return response

    def test_get_blog_page(self):
        return self.get_page_200('blog:blog')

    def test_blogpage_shows_articles(self):
        response = self.test_get_blog_page()
        # there should be three articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 3)
        # and there should be three categories on the page
        numcat = len(response.context['categories'])
        self.assertEqual(numcat, 3)

    def test_categ_has_articles(self):
        response = self.get_page_200('blog:categarticles',
                                     kwargs={'pk': self.catmusic.id, })
        # there should be two articles on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 2)

    def test_author_has_articles(self):
        response = self.get_page_200('blog:authorarticles',
                                     kwargs={'pk': self.author.id, })
        # there should be one article on the page
        numart = len(response.context['object_list'])
        self.assertEqual(numart, 1)

    def test_createnewarticle(self):
        logged = self.client.login(username='pinom', password='xyzxyz')
        self.assertTrue(logged)
        ARTICLE_TITLE = "Post test"
        with open('blog/tests/my_test_image.jpg') as imgf:
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

    def test_contact_form(self):
        logged = self.client.login(username='pinom', password='xyzxyz')
        self.assertTrue(logged)
        post_data = {'name': "pippo",
                     'email_address': "pippo@pluto.com",
                     'message': "hey your blog really sucks!"}
        response = self.client.post(reverse('blog:contact'),
                                    data=post_data)
    # it should be redirected temp. HTTP 302
        self.assertRedirects(response, reverse('blog:blog'), status_code=302)
        # there should be one msg
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn("sucks", mail.outbox[0].body)

    @staticmethod
    def is_reverse_sorted(x, key = lambda x: x):
        return all([key(x[i]) >= key(x[i + 1]) for i in xrange(len(x) - 1)])

    def test_stats_page(self):
        response = self.get_page_200('blog:stats')

        self.assertIn('stats4authors', response.context)
        stats4authors = response.context['stats4authors']
        self.assertLessEqual(len(stats4authors), 10)
        self.assertTrue(self.is_reverse_sorted(stats4authors,
                                               key=lambda x: x.numarticles),
                        msg="stats4authors is not reverse-sorted!")

        self.assertIn('stats4categories', response.context)
        stats4categories = response.context['stats4categories']
        self.assertLessEqual(len(stats4categories), 10)
        self.assertTrue(self.is_reverse_sorted(stats4categories,
                                               key=lambda x: x.numarticles),
                        msg="stats4categories is not reverse-sorted!")

    def test_fail(self):
        self.fail("Testing ain't over yet")

