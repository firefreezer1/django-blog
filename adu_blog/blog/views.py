from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def home(request):
    posts = Post.objects.filter(approved=True)
    return render(request, 'home.html', {'posts': posts})


def blog_form(request):

    if request.method == 'GET':
        return render(request, 'input.html')

    try:
        post = Post()
        post.title = request.POST['title']
        post.author = request.POST['name']
        post.body = request.POST['message']
        post.publish()
        return render(request, 'input.html')
    except Exception as e:
        print(e)


def post_page(request, post_uuid):
    try:
        post = Post.objects.get(id=post_uuid)
        return render(request, 'post.html', {'post': post})
    except Exception as e:
        print(e)
