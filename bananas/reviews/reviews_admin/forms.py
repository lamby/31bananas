from django import forms

from ..models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = (
            'title',
            'source',
            'price',
            'content',
            'published',
            'nutrition',
            'score_banana',
            'score_overall',
            'nutrition_serving',
        )
