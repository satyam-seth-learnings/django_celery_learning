from django.http import HttpResponse
from django.shortcuts import render
from .task import test_func

# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")