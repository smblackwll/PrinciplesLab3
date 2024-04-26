from django.shortcuts import render, redirect

from home.forms import CommentForm
from home.models import Comment


def home(request):
    return render(request, 'home.html')

def sam(request):
    return render(request, 'sam.html')

def kj(request):
    return render(request, 'kj.html')

def spencer(request):
    return render(request, 'spencer.html')

def tim(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.related_page = "tim"  # Ensure this matches how you identify pages
            comment.save()
            return redirect('tim')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(related_page="tim")


    return render(request, 'tim.html',
                  {'comments': comments,
                   'form': form})
