from django.forms import ModelForm, HiddenInput

from kb.models import Article, Image, File


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description']


class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['article', 'image']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super(ImageForm, self).__init__(*args, **kwargs)
        self.fields['article'].widget = HiddenInput()
        self.fields['article'].initial = Article.objects.get(pk=self.pk)


class FileForm(ModelForm):
    class Meta:
        model = File
        fields = ['article', 'file']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super(FileForm, self).__init__(*args, **kwargs)
        self.fields['article'].widget = HiddenInput()
        self.fields['article'].initial = Article.objects.get(pk=self.pk)



