import StringIO

from PIL import Image

from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.core.files.base import ContentFile
from django.views.decorators.http import require_POST

from bananas.utils.ajax import ajax, json_render
from bananas.utils.decorators import superuser_required

from ...models import Review

from .forms import ImageForm, URLForm

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
def xhr_add_url(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    form = URLForm(review, request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "Image added.")
    else:
        messages.error(request, "There was an error adding this image.")

    return json_render(request, 'reviews/admin/images/xhr_view.html', {
        'review': review,
    })

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

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_rotate(request, review_id, image_id):
    review = get_object_or_404(Review, pk=review_id)

    image = get_object_or_404(review.images, pk=image_id)

    fileobj = StringIO.StringIO()
    im = Image.open(image.image.original.open())
    im.rotate(-90).save(fileobj, 'JPEG')

    image.image.save(ContentFile(fileobj.getvalue()))
    image.image.cachebust()
    image.save()

    messages.success(request, "Image rotated.")

    return json_render(request, 'reviews/admin/images/xhr_view.html', {
        'review': review,
    })

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_move_right(request, review_id, image_id):
    review = get_object_or_404(Review, pk=review_id)
    image = get_object_or_404(review.images, pk=image_id)

    try:
        next_ = review.images.filter(order__gt=image.order)[0]
    except IndexError:
        messages.success(request, "Image not moved.")
    else:
        order_ = image.order
        image.order = -1
        image.save(update_fields=('order',))

        # Swap
        image.order, next_.order = next_.order, order_
        next_.save(update_fields=('order',))
        image.save(update_fields=('order',))

        messages.success(request, "Image moved.")

    return json_render(request, 'reviews/admin/images/xhr_view.html', {
        'review': review,
    })
