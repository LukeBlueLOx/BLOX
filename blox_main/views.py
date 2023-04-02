from django.shortcuts import render

def index(request):
    return render(request, 'blox_main/index.html', {})
