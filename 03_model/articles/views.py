from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    #<QuerySet [<Article:django, <Article:>....]
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    #DB에 새로운 게시글 생성
    #방법1
    '''
    article = Article()
    article.title = title
    article.content = content
    article.save()
    '''
    #방법2
    '''
    article = Article(title=title, content=content)
    article.save()
    '''
    #방법3
    Article.objects.create(title=title, content=content)
    return render(request, 'articles/index.html')