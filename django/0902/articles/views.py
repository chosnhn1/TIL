from django.http import request
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    # articles = Article.objects.all()[::-1]  # order by python
    articles = Article.objects.order_by('-id')  # order by ORM
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

def new(request):

    return render(request, 'articles/new.html')

def create(request):
    print(request.POST) # GET: DB 쓰기 없음 / 민감하지 않은 정보 등
    title = request.POST.get('title')        # template의 name으로 넘어온 것
    content = request.POST.get('content')

    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # article = Article(title, content)

    article = Article(title=title, content=content)
    # Vaildation and Processing will be written here
    article.save()

    return redirect('articles:detail', article.pk)
    # return render(request, 'articles/create.html')

def detail(request, pk):                # variable routing
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }

    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()

    return redirect('articles:detail', article.pk)