from django.contrib import admin
from django.contrib.admin import ModelAdmin

from kb.functions import fetch_html, extract_urls, extract_description, extract_title
from kb.models import Article, Image, File, Page


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1


class FileInline(admin.TabularInline):
    model = File
    extra = 1


class ArticleAdmin(ModelAdmin):

    model = Article
    readonly_fields = ['slug']
    list_display = ['pk', 'title']
    inlines = [ImageInline, FileInline]


admin.site.register(Article, ArticleAdmin)


def fetch_html_admin(modeladmin, request, queryset):

    for page in queryset:

        if not page.html:
            html = fetch_html(page.url)
            page.html = html
            page.fetched_html = True
            page.save()


fetch_html_admin.short_description = '01. Fetch HTML'


def extract_urls_admin(modeladmin, request, queryset):

    for page in queryset:

        urls = extract_urls(page.html)

        for url in urls:

            _page, created = Page.objects.get_or_create(url=url)

            if created:
                _page.parent = page
                _page.save()

        page.extracted_urls = True
        page.save()


extract_urls_admin.short_description = '02. Extract Urls'


def extract_title_admin(modeladmin, request, queryset):

    for page in queryset:

        title = extract_title(page.html)

        page.title = title
        page.extracted_title = True
        page.save()


extract_title_admin.short_description = '03. Extract Title'


def extract_description_admin(modeladmin, request, queryset):

    for page in queryset:

        description = extract_description(page.html)

        page.description = description
        page.extracted_description = True
        page.save()


extract_description_admin.short_description = '04. Extract Description'


def convert_article_admin(modeladmin, request, queryset):

    for page in queryset:

        article, created = Article.objects.get_or_create(title=page.title)

        article.description = page.description
        article.url = page.url
        article.save()

        page.converted_article = True
        page.save()


convert_article_admin.short_description = '05. Convert to Article'


class PageAdmin(ModelAdmin):

    model = Page
    list_display = ['pk', 'url', 'fetched_html', 'extracted_urls', 'extracted_title', 'extracted_description', 'converted_article']
    actions = [fetch_html_admin, extract_urls_admin, extract_title_admin, extract_description_admin, convert_article_admin]


admin.site.register(Page, PageAdmin)


class ImageAdmin(ModelAdmin):

    model = Image
    list_display = ['article', 'image']


admin.site.register(Image, ImageAdmin)


class FileAdmin(ModelAdmin):

    model = File
    list_display = ['article', 'file']


admin.site.register(File, FileAdmin)

admin.site.site_header = 'Web Developer Challenge'
admin.site.site_title = 'Web Developer Challenge'

