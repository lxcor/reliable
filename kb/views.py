from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from vanilla import ListView, CreateView, UpdateView, DeleteView, DetailView

from kb.forms import ArticleForm, ImageForm, FileForm
from kb.models import Article


class ListArticles(ListView):
    model = Article


class CreateArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'kb/article_create.html'
    success_url = reverse_lazy('list-articles')


class EditArticle(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'kb/article_edit.html'
    success_url = reverse_lazy('list-articles')


class DeleteArticle(DeleteView):
    model = Article
    template_name = 'kb/article_delete.html'
    success_url = reverse_lazy('list-articles')


class ReadArticle(DetailView):
    model = Article
    template_name = 'kb/article_read.html'


def upload_image(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':

        form = ImageForm(request.POST, request.FILES, pk=pk)

        if form.is_valid():

            form.save()
            article.save()

            return HttpResponseRedirect(reverse_lazy('read-article', kwargs={'pk': pk}))

    else:

        form = ImageForm(pk=pk)

    context = {'form': form, 'article': article}

    return render(request, 'kb/image_upload.html', context)


def upload_file(request, pk):

    article = get_object_or_404(Article, pk=pk)

    if request.method == 'POST':

        form = FileForm(request.POST, request.FILES, pk=pk)

        if form.is_valid():

            form.save()
            article.save()

            return HttpResponseRedirect(reverse_lazy('read-article', kwargs={'pk': pk}))

    else:

        form = FileForm(pk=pk)

    context = {'form': form, 'article': article}

    return render(request, 'kb/file_upload.html', context)
