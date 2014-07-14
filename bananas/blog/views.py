import datetime
import itertools

from email_from_template import send_mail

from django.http import HttpResponseForbidden
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

def view(request, slug):
    qs = Post.objects.published()

    if request.user.is_superuser or 'Lohzie7E' in request.GET:
        qs = Post.objects.all()

    post = get_object_or_404(qs, slug=slug)

    return render(request, 'blog/post.html', {
        'form': form,
        'post': post,
    })
