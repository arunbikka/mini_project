from django.shortcuts import render

posts = [
    {
        'author': 'arun kumar',
        'title': 'python project',
        'posted' : 'august'
    },
    {
        'author': 'arun',
        'title': 'python ',
        'posted' : 'august'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title':'About'})
