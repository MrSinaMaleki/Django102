from django.shortcuts import render, redirect, get_object_or_404
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


def delete(request, post_id):

    obj = get_object_or_404(Post, id=post_id)

    obj.delete()
    print("post was deleted!")
    return redirect('home')
