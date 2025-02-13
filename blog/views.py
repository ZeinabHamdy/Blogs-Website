from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from .forms import EmailPostForm
from .models import Post
from django.conf import settings




def post_list(req):
    posts = Post.published.all()
    paginator = Paginator(posts, 4) 
    page_number = int(req.GET.get('page')) # as req.GET.get('page') returns a string
    error_message =''
    if page_number > paginator.num_pages:
        error_message = 'Page number must be less than or equal to the total number of pages'
    elif page_number < 1 :
        error_message ='Page number must be greater than 0'
    elif page_number is float:
        error_message = 'Page number must be an integer'
        
    if error_message != '':
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
    if req.method == 'POST':
        form = EmailPostForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['name'],
                cd['comments'],
                settings.EMAIL_HOST_USER,
                [cd['email_to']],
                fail_silently=False,
            )
            
            return redirect('forms_success') 
    else:
        form = EmailPostForm() # empty form
    context = {
        'post': post,
        'form': form,
    }
    return render(req, 'post_share.html', context)



def forms_success(req):
        return render(req, 'forms_success.html')