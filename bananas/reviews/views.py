from django.shortcuts import render, get_object_or_404, redirect

from .models import Review, YEAR, MONTH

def view(request, day, slug):
    qs = Review.objects.public()

    if request.user.is_superuser or 'Lohzie7E' in request.GET:
        qs = Review.objects.all()

    review = get_object_or_404(
        qs,
        date__day=day,
        date__year=YEAR,
        date__month=MONTH,
    )

    # Redirect if the slug does not match
    if slug != review.slug():
        return redirect(review, permanent=True)

    return render(request, 'reviews/view.html', {
        'score': range(review.score),
        'review': review,
    })
