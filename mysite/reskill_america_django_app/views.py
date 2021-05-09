from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse



data = {
    'Name': 'Marco Apraez',
    'Track': 'Python-Backend-Track',
    'Message': 'I believe I\'ve followed directions correctly.'
}

# Create your views here.
def test_function_name(request):
    return JsonResponse(data)
