from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def drink(request):
    return render(request, 'pages/drink.html')

def dinner(request, 저녁메뉴, 인원수):
    context = {
        '저녁메뉴': 저녁메뉴,
        '인원수': 인원수,
    }
    return render(request, 'dinner.html', context)