from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.http import require_POST
from django.views.decorators.cache import never_cache

from bananas.utils.ajax import ajax, json_render
from bananas.utils.decorators import superuser_required

from ..models import Post

from .forms import PostForm, CoverForm

@never_cache
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            next = request.GET.get('next', settings.LOGIN_REDIRECT_URL)

            auth.login(request, form.get_user())

            return HttpResponseRedirect(next)
    else:
        form = AuthenticationForm(request)

    request.session.set_test_cookie()

    return render(request, 'blog/admin/login.html', {
        'form': form,
    })

@superuser_required
def index(request):
    posts = Post.objects.filter(
        published__isnull=True,
    ).order_by(
        '-created',
    )

    return render(request, 'blog/admin/index.html', {
        'posts': posts,
    })

@superuser_required
def add(request):
    post = Post.objects.create()

    for tag in Tag.objects.planets():
        post.tags.add(tag)

    return redirect('blog:admin:edit', post.pk)

@superuser_required
def edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    return render(request, 'blog/admin/edit.html', {
        'post': post,
        'form': PostForm(instance=post),
    })

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    form = PostForm(request.POST, instance=post)

    if not form.is_valid():
        messages.error(request, "There was an error saving this post.")
        return json_render(request)

    old_published = post.published

    post = form.save()

    if post.published == old_published:
        messages.success(request, "Post saved.")
    else:
        messages.success(request, "Post published.")

    return json_render(request)

@require_POST
@superuser_required
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    post.delete()

    messages.success(request, "Post deleted.")

    return redirect('blog:admin:index')

@require_POST
@ajax(login_required=True)
@superuser_required
def xhr_cover_url(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    form = CoverForm(request.POST, instance=post)

    if form.is_valid():
        form.save()
        messages.success(request, "Cover updated.")
    else:
        messages.error(request, "Could not parse URL.")

    return json_render(request)

@superuser_required
def moderate_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.is_moderated = True
    comment.save()

    messages.success(request, "Comment moderated.")

    return redirect(comment)
