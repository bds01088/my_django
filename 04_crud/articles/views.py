from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

#create에서 method가 post가 아니면 그냥 new.html을 보여주기 때문에
#new가 독립적으로 있을 필요가 없어짐
#def new(request):
#    return render(request, 'articles/new.html')

def create(request):
    #사용자가 POST요청을 보냈다면
    if request.method == 'POST' :
        #new.html에 input태그에 name을 키값으로 가져옴
        #GET은 Read만 함
        #title = request.GET.get('title')
        #content = request.GET.get('content')
        title = request.POST.get('title')
        content = request.POST.get('content')
        '''
        Article.objects.create(title=title, content=content)
        '''
        article = Article()
        article.title = title
        article.content = content
        article.save()

        #POST 요청에 맞게 생성한 뒤
        #return render(request, 'articles/index.html')
        #단순히 index.html을 불러오는게 아니라
        #새로 생성된 데이터를 받아서 새로운 값을 표시해주어야함
        #즉 views.index를 재실행시킨다는 느낌
        #index페이지를 GET해주는 것이 redirect이고, django.shortcut에 import해주어야함
        return redirect('articles:detail', article.pk)
    #아니면~
    #create페이지에서 제목이랑 내용이 비어있다면..
    #서버에러(500)라고 뜨지만 이건 서버문제가 아니라 이상한 값을 넣은 사용자 문제
    #else :
    #GET요청이 오면 html문서를 보여주자
    #return render(request, 'articles/new.html')
    #update와 골조가 유사해 통합한 form사용
    return render(request, 'articles/form.html')

def detail(request, article_pk):
    #article_pk번째 게시글의 정보를 조회,반영
    #article = Article.objects.get(pk=article_pk)
    #article_pk가 없는걸 조회한다면
    #import get_obejct_or_404 해서
    #함수에 테이블명, 조건 입력
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method == 'POST' :
        #article = Article.objects.get(pk=article_pk)
        article = get_object_or_404(Article, pk=article_pk)
        #삭제 orm
        article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    #article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST' :
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else :
        context = {
            'article' : article
        }
    #if문 도중 어느 조건에 의해 튕겨져 나오는 것까지 커버치기 위해 else문에 안넣음
    #create와 골조가 유사해 form으로 통합함
    return render(request, 'articles/form.html', context)