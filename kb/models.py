from django.contrib.auth.models import User
from django.db import models
from django.db.models import DO_NOTHING, CASCADE
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.text import slugify


class Article(models.Model):

    title = models.CharField(max_length=255, help_text="Enter the article title here. Up to 255 characters.")
    description = models.TextField(help_text="Enter the content of the article here. Any length.")
    slug = models.SlugField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    n_images = models.PositiveSmallIntegerField(null=True, blank=True, default=0)
    n_files = models.PositiveSmallIntegerField(null=True, blank=True, default=0)

    class Meta:
        ordering = ('pk', 'title')

    def save(self, *args, **kwargs):

        if self.pk is None:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()

        self.slug = slugify("%s" % self.title)

        self.n_images = self.image_set.all().count()
        self.n_files = self.file_set.all().count()

        return super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return "%s" % self.title


class Image(models.Model):

    article = models.ForeignKey(Article, on_delete=CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name=" image ")

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return "%s" % self.pk


class File(models.Model):

    article = models.ForeignKey(Article, on_delete=CASCADE)
    file = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return "%s" % self.pk


class Page(models.Model):
    parent = models.ForeignKey('self', on_delete=CASCADE, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    html = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    fetched_html = models.BooleanField(default=False)
    extracted_urls = models.BooleanField(default=False)
    extracted_title = models.BooleanField(default=False)
    extracted_description = models.BooleanField(default=False)
    converted_article = models.BooleanField(default=False)

    def __str__(self):
        return "%s" % self.url
