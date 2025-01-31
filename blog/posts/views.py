from django.shortcuts import render
from .models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, "posts/list.ptml", {"posts": posts})

def post_details(request):
    posts = Post.objects.get(ig=post_id)
    return render(request, "posts/list.ptml", {"posts": posts})