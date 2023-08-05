from django.shortcuts import render

posts = [
    {
        'author': 'Emmanuel',
        'title': 'My First Blog',
        'content': 'Content of my first blog',
        'date_posted': 'August 8th 2023'
    },
    {
        'author': 'Tony Star',
        'title': 'Iron Man 4',
        'content': 'Iron Man 4 is about get released coming month....',
        'date_posted': 'August 10th 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})