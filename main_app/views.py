from django.shortcuts import render


cats = [
    {
        "name": "Lolo",
        "breed": "tabby",
        "description": "furry little demon",
        "age": 3,
    },
        {
        "name": "Sachi",
        "breed": "calico",
        "description": "gentle and loving",
        "age": 2,
    },
]

# Create your views here.

#home view
def home(request):
    return render(request, 'home.html')

#about view
def about(request):
    return render(request, 'about.html')

#cats view
def cats_index(request):
    return render(request, 'cats/index.html', {
        'cats': cats
    })