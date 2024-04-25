from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def sam(request):
    return render(request, 'sam.html')

def kj(request):
    return render(request, 'kj.html')

def spencer(request):
    return render(request, 'spencer.html')

def tim(request):
    return render(request, 'tims_page.html')