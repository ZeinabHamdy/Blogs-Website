from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post



def post_list(req):
    posts = Post.published.all()
    paginator = Paginator(posts, 4) # Show 4 posts per page
    page_number = int(req.GET.get('page')) # as req.GET.get('page') returns a string
    if page_number > paginator.num_pages:
        return render(req, 'blog/error.html', {'error_message': 'Page number must be less than or equal to the total number of pages'} )
    elif page_number < 1 :
        return render(req, 'blog/error.html', {'error_message': 'Page number must be greater than 0'} )
    elif page_number is float:
        return render(req, 'blog/error.html', {'error_message': 'Page number must be an integer'})


    posts = paginator.get_page(page_number)
    context = {
        'page': page_number,
        'posts': posts,
        'total_pages': paginator.num_pages,
    }
    return render(req, 'blog/posts.html', context)


def post_details(req, pk):
    post = get_object_or_404(Post.published, pk=pk)
    context = {
        'post': post,
        'title': post.title,
    }
    return render(req, 'blog/posts.html', context)