from django.shortcuts import render
from .models import Post, Author
import re

# Create your views here.
def post_list(request):
    post = Post.objects.all()
    author = Author.objects.all()
    return render(request, 'blog/post_list.html', {'posts': post, 'authors':author})

# def post_new(request):
#     return render(request, 'blog/post_new.html')

# def post_detail(request, id):
