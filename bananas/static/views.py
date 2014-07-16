from django.shortcuts import render

from bananas.reviews.models import Review

def landing(request):
    return render(request, 'static/landing.html', {
        'reviews': Review.objects.public(),
    })
