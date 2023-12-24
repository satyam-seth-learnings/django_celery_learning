from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub

# Enqueue Task using delay()
def index(request):
    print("Results: ")
    # result1 = add(10, 20)
    result1 = add.delay(10, 20)
    print('Result 1: ', result1)
    result2 = sub.delay(30, 20)
    print('Result 2: ', result2)
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def contact(request):
    return render(request, 'myapp/contact.html')