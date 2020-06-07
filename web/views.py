from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'home/home.html')


def sports(request):
    # Todo: Sort the Posts and bring only the Sports Posts to this section
    sportnews = Post.objects.filter(category=1)
    context = {"sportsnews": sportnews}
    return render(request, 'sports/sports.html', context)


def about(request):
    return render(request, 'about/about.html')


def contact(request):
    return render(request, 'contact/contact.html')


def details(request):
    return render(request, 'singlepost/singlepost.html')
