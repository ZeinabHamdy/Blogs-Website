from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(req):
    posts = Post.published.all()
    # to appear only published posts
    context = {
        'posts': posts,
    }
    return render(req, 'blog/posts.html', context)


def post_details(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(req, 'blog/posts.html', context)