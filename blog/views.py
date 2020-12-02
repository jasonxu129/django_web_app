from django.shortcuts import render

posts = [
    {
        'author': 'JasonXu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Nov 29, 2020'
    },
    {
        'author': 'Lebron James',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Nov 30, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
