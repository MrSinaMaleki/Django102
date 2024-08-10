from django.shortcuts import render
from .forms import CreatePostForm


# Create your views here.

def test(request):
    return render(request, 'test.html')


def create_post(request):
    # context = {'form': CreatePostForm()}
    context = dict()
    form = CreatePostForm(request.POST or None)

    if form.is_valid():
        form.save()

    context['form'] = form

    return render(request, 'add_posts.html', context)
