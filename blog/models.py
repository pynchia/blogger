from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)
    descr = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = 'categories'
    def __unicode__(self):
        return u"%s" % self.name


class Article(models.Model):
    author = models.ForeignKey(User, editable=False)
    published_on = models.DateTimeField(auto_now_add=True, editable=False)
    categories = models.ManyToManyField(Category,
                                        help_text='as many as necessary')
    title = models.CharField(max_length=128,
                             help_text='concise but useful')
    body = models.TextField(help_text='the content')
    tags = models.CharField(max_length=128, blank=True,
                            help_text='space or comma separated')
    IMG_MAX_WIDTH = 256
    IMG_MAX_HEIGHT = 160
    image = models.ImageField(upload_to='articleimg',
                              help_text='optimal size %dx%d pixels' % (
                                            IMG_MAX_WIDTH, IMG_MAX_HEIGHT))

    def __unicode__(self):
        return u"%s" % self.title
