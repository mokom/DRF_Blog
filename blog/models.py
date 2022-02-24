import imp
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey("blog.Category", verbose_name=_("Category"), on_delete=models.PROTECT, default=1)
    title = models.CharField(_("Title"), max_length=250)
    excerpt = models.TextField(_("Excerpt"), null=True)
    content = models.TextField(_("Content"))
    slug = models.SlugField(_("Slug"), max_length=250, unique_for_date='published')
    published = models.DateTimeField(_("Published"), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(_("Status"), max_length=10, choices=options, default='published')
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title