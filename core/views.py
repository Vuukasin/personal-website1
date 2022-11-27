from django.shortcuts import render

# Create your views here.

def home_view(request):
    context = {}
    return render(request, 'home.html', context)


def blog_view(request):
    context = {}
    return render(request, 'blog.html', context)

def resume_view(request):
    context = {}
    return render(request, 'resume.html', context)


