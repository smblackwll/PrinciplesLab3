from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from home.forms import CommentForm
from home.models import Comment


def home(request):
    return render(request, 'home.html')


@login_required
def sam(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.related_page = "sam"  # Ensure this matches how you identify pages
            comment.save()
            return redirect('sam')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(related_page="sam")


    return render(request, 'sam.html',
                  {'comments': comments,
                   'form': form})


@login_required
def kj(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.related_page = "kj"  # Ensure this matches how you identify pages
            comment.save()
            return redirect('kj')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(related_page="kj")


    return render(request, 'kj.html',
                  {'comments': comments,
                   'form': form})


@login_required
def spencer(request):
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.related_page = "spencer"  # Ensure this matches how you identify pages
            comment.save()
            return redirect('spencer')
    else:
        form = CommentForm()

    comments = Comment.objects.filter(related_page="spencer")


    return render(request, 'spencer.html',
                  {'comments': comments,
                   'form': form})

@login_required
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
