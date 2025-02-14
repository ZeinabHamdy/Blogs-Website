from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import EmailPostForm
from .models import Post
from django.conf import settings




def post_list(req):
    posts = Post.published.all()
    paginator = Paginator(posts, 4) 
    page_number = req.GET.get('page', '1') # as req.GET.get('page') returns a string
    error_message =''

    try:
        page_number = int(page_number) 
        if page_number < 1:
            error_message = 'Page number must be greater than 0'
        elif page_number > paginator.num_pages:
            error_message = 'Page number must be less than or equal to the total number of pages'
    except ValueError:
        error_message = 'Page number must be an integer'
        
    if error_message :
        return render(req, 'error.html', {'error_message': error_message})

    posts = paginator.get_page(page_number)
    context = {
        'page': page_number,
        'posts': posts,
        'total_pages': paginator.num_pages,
    }
    return render(req, 'posts.html', context)



def post_details(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(req, 'posts.html', context)



def post_share(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    sent = False
    if req.method == 'POST':
        form = EmailPostForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = req.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} ({cd['email_to']}) recommends you read \'{post.title}\' --- '{cd['subject']}' "
            message = f"Read \'{post.title}\' at {post_url}\n\n{cd['name']}'s comments: {cd['comments']}"
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [cd['email_to']])
            sent = True
    else:
        form = EmailPostForm()
    context = {
        'post': post,
        'form': form,
        'sent': sent,
    }
    return render(req, 'post_share.html', context)
