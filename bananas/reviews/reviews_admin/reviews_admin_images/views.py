from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from bananas.utils.ajax import ajax, json_render
from bananas.utils.decorators import superuser_required

from ...models import Review

from .forms import ImageForm

@ajax(login_required=True)
@superuser_required
def xhr_view(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    return json_render(request, 'reviews/admin/images/xhr_view.html', {
        'review': review,
    })

@require_POST
@superuser_required
def add(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    form = ImageForm(review, request.POST, request.FILES)

    if form.is_valid():
        form.save()
        messages.success(request, "Image added.")
    else:
        messages.error(request, "There was an error adding this image.")

    return redirect('reviews:admin:edit', review.pk)

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_delete(request, review_id, image_id):
    review = get_object_or_404(Review, pk=review_id)

    get_object_or_404(review.images, pk=image_id).delete()

    messages.success(request, "Image deleted.")

    return json_render(request, 'reviews/admin/images/xhr_view.html', {
        'review': review,
    })
