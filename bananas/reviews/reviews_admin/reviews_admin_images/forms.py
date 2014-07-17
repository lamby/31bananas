import io
import urllib

from django import forms
from django.db import models
from django.core.files import File

from ...models import Image

class ImageForm(forms.ModelForm):
    image = forms.ImageField()

    class Meta:
        model = Image
        fields = ()

    def __init__(self, review, *args, **kwargs):
        self.review = review

        super(ImageForm, self).__init__(*args, **kwargs)

    def save(self):
        max_order = self.review.images.aggregate(
            order=models.Max('order'),
        )['order'] or 0

        instance = super(ImageForm, self).save(commit=False)
        instance.order = max_order + 1
        instance.review = self.review
        instance.save()

        instance.image.save(self.cleaned_data['image'])
        instance.save()

        return instance

class URLForm(ImageForm):
    image = forms.URLField()

    def clean_image(self):
        fileobj = urllib.urlopen(self.cleaned_data['image'])

        return File(io.BytesIO(fileobj.read()))
