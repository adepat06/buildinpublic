from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


@login_required
def feed(request):

    if request.method == "POST":

        if "create_post" in request.POST:

            form = PostForm(request.POST)

            if form.is_valid():

                post = form.save(commit=False)
                post.user = request.user
                post.save()

                return redirect("feed")

        elif "add_comment" in request.POST:

            comment_form = CommentForm(request.POST)

            post = get_object_or_404(
                Post,
                id=request.POST.get("post_id")
            )

            if comment_form.is_valid():

                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()

                return redirect("feed")

    form = PostForm()
    comment_form = CommentForm()

    posts = Post.objects.all()

    return render(
        request,
        "social/feed.html",
        {
            "form": form,
            "comment_form": comment_form,
            "posts": posts,
        },
    )


@login_required
def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():

        post.likes.remove(request.user)

    else:

        post.likes.add(request.user)

    return redirect("feed")


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        user=request.user
    )

    post.delete()

    return redirect("feed")