from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm


@login_required
def feed(request):

    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.user

            post.save()

            return redirect('feed')

    else:

        form = PostForm()

    posts = Post.objects.all()

    return render(
        request,
        'social/feed.html',
        {
            'form': form,
            'posts': posts
        }
    )