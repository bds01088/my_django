from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')
    
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    message = request.GET.get('articles/message')
    context = {
        'message' : message
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'articles/hello.html', context)