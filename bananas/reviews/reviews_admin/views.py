import calendar
import datetime

from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache

from bananas.utils.ajax import ajax, json_render
from bananas.utils.decorators import superuser_required

from ..models import Review, YEAR, MONTH

from .forms import ReviewForm

@never_cache
def login(request):
    if request.user.is_authenticated():
        return redirect('reviews:admin:index')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            next = request.GET.get('next', settings.LOGIN_REDIRECT_URL)

            auth.login(request, form.get_user())

            return HttpResponseRedirect(next)
    else:
        form = AuthenticationForm(request)

    request.session.set_test_cookie()

    return render(request, 'reviews/admin/login.html', {
        'form': form,
    })

@superuser_required
def index(request):
    c = calendar.Calendar()
    by_day = {x.date: x for x in Review.objects.all()}

    return render(request, 'reviews/admin/index.html', {
        'days': c.monthdatescalendar(YEAR, MONTH),
        'by_day': by_day,
        'reviews': Review.objects.all(),
    })

@superuser_required
def edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    return render(request, 'reviews/admin/edit.html', {
        'form': ReviewForm(instance=review),
        'review': review,
    })

@superuser_required
def move_down(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    try:
        next_ = Review.objects.filter(date__gt=review.date)[0]
    except IndexError:
        pass
    else:
        date_ = review.date
        review.date = datetime.date.min
        review.save(update_fields=('date',))

        # Swap
        review.date, next_.date = next_.date, date_
        next_.save(update_fields=('date',))
        review.save(update_fields=('date',))

    return redirect('reviews:admin:index')

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_edit(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    form = ReviewForm(request.POST, instance=review)

    if not form.is_valid():
        messages.error(request, "There was an error saving this review.")
        return json_render(request)

    review = form.save()
    messages.success(request, "Review saved.")

    return json_render(request)
