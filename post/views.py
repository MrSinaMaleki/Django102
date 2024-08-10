from django.shortcuts import render, redirect
from .models import Post
from .forms import CreatePostForm
from django.urls import reverse


# Create your views here.

def home(request):
    return render(request, 'home.html', {"posts": Post.objects.all()})


def create_post(request):
    # context = {'form': CreatePostForm()}
    context = dict()
    form = CreatePostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
        return redirect('home')

    context['form'] = form
    # context['target_url'] = reverse('home')

    return render(request, 'add_posts.html', context)
