from articles.models import Article
from django.shortcuts import render, redirect
from .forms import ArticleForm
from django.views.decorators.http import require_http_methods, require_POST, require_safe

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # form에 입력값 받기
        form = ArticleForm(data=request.POST)
        if form.is_valid(): 
            article = form.save()
            # 글 올려주고 redirect하기
            return redirect('articles:detail', article.pk)
    else:
        # empty form 
        form = ArticleForm()    # make instance
    
    context = {                 # serve instance
        'form': form,
    }
    # (빈 / 도로 담은) form 돌려주기
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'article': article,      # for article.pk, redirection
        'form': form,
    }
    return render(request, 'articles/update.html', context)