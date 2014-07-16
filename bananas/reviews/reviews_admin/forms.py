from django import forms

from ..models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'source',
            'price',
            'score',
            'content',
            'nutrition',
            'nutrition_serving',
            'published'
        )
