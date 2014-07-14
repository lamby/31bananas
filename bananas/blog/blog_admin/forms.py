import io
import urllib
import datetime

from django import forms
from django.core.files import File

from bananas.blog.models import Post

class PostForm(forms.ModelForm):
    publish = forms.BooleanField(required=False)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'slug',
        )

    def clean(self):
        if self.cleaned_data['publish'] or self.instance.published:
            if not self.cleaned_data['title']:
                raise forms.ValidationError("Title missing")

            if not self.cleaned_data['content']:
                raise forms.ValidationError("No content")

        return self.cleaned_data

    def clean_slug(self):
        return self.cleaned_data.get('slug') or None

    def save(self):
        post = super(PostForm, self).save(commit=False)

        if self.cleaned_data['publish']:
            post.published = datetime.datetime.utcnow()

        post.save()

        return post

class CoverForm(forms.ModelForm):
    url = forms.URLField()

    class Meta:
        model = Post
        fields = ()

    def clean_url(self):
        fileobj = urllib.urlopen(self.cleaned_data['url'])

        self.cleaned_data['cover'] = File(io.BytesIO(fileobj.read()))

    def save(self):
        self.instance.cover.save(self.cleaned_data['cover'])
        self.instance.has_cover = True
        self.instance.save()
