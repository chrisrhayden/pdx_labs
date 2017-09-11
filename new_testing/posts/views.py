from django.shortcuts import render
from .models import BlogPost


# Create your views here.


def show_post(request):

    post = BlogPost.objects.latest('created')
    context = {'post': post}
    return render(request, 'index.html', context)
