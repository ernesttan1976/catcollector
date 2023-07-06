from django.shortcuts import render

from .models import Cat


#home view
def home(request):
    return render(request, 'home.html')

#about view
def about(request):
    return render(request, 'about.html')

#cats view
def cats_index(request):
    cats = Cat.objects.all().order_by("id")
    return render(request, 'cats/index.html', {
        'cats': cats
    })

#cats detail view
def cats_detail(request, cat_id):
    # cat = Cat.objects.filter(id=cat_id)[0]
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {
        'cat': cat
    })