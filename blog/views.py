# by me
from .forms import EmailPostForm, AddPost
from .models import Post


# by default
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings



def post_list(req):
    posts = Post.published.all()
    paginator = Paginator(posts, 5)  # Show 5 posts per page
    page_number = req.GET.get('page', '1')

    try:
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage: # out of range
        posts = paginator.get_page(paginator.num_pages)

    context = {
        'posts': posts,
        'total_pages': paginator.num_pages,
        'title': 'Posts',
    }
    return render(req, 'posts.html', context)


def post_details(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    context={
        'post': post,
        'title':post.title,
    }
    return render(req, 'post_details.html', context)


@login_required
def post_share(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    sent = False

    if req.method == 'POST':
        form = EmailPostForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = req.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read '{post.title}' — {cd['subject']}"
            message = f"Read '{post.title}' at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['email_to']])
            sent = True
    else:
        form = EmailPostForm()

    context = {
        'post': post,
        'form': form,
        'sent': sent,
        'title': f'Share a post "{post.title}"',
    }
    return render(req, 'post_share.html', context)



@login_required
def add_post(req):
    if req.method == 'POST':
        form = AddPost(req.POST)
        if form.is_valid():
            new_post = Post.objects.create(
                author=req.user,
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                status=form.cleaned_data['status'],
            )
            new_post.save()
            return redirect('home')
    else :
        form = AddPost()

    context = {
        'form': form,
        'title': 'add a new post',
    }
    return render(req, 'add_edit_post.html', context)


@login_required
def edit_post(req, pk):
    post = Post.objects.get(id=pk)

    if req.user != post.author:
        messages.error(req, "You can't access this page")
        return redirect('home')

    if req.method == 'POST':
        form = AddPost(req.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPost(instance=post)

    context = {
        'form': form,
        'title': 'edit your post',
    }
    return render(req, 'add_edit_post.html', context)