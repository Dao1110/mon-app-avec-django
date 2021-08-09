from django.core import paginator
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def post_list(request):
    objects_list = Post.objects.all()
    paginator = Paginator(objects_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts' : posts,
        'page' : page 
    }
    return render(request, 'blog/post/list.html', {'posts': context })


def post_detail(request, slug:str):
    try:
        post =Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise('This post dosenot exist')
    return render(request, 'blog/post/detail.html', {'post':post})


