from django.shortcuts import render

from datetime import datetime
import random

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def introduce(request):
    return render(request, 'articles/introduce.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name': 'CSH',

    }

    context = {
        'info': info,
        'foods': foods,
    }

    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['연어', '광어', '참돔', '참다랑어', '우럭']
    pick = random.choice(foods)

    context = {
        'pick': pick,
        'foods': foods,
        'no':'1'

    }
    return render(request, 'articles/dinner.html', context)

def image(request):

    return render(request, 'articles/image.html')

def template_language(request):
    menus = ['연어', '광어', '우럭', '참돔']
    my_sentence = 'We Race As One'
    messages = ['apple', 'banana', 'coconut', 'mango',]
    datetimenow = datetime.now()
    empty_list = []


    context = {
        'menus': menus,
        'my_sentence': my_sentence,
        'messages': messages,
        'datetimenow': datetimenow,
        'empty_list': empty_list,
    }

    return render(request, 'articles/template_language.html', context)

def throw(request):
    
    return render(request, 'articles/throw.html')

def catch(request):
    print(request.GET)
    message = request.GET.get('message')
    context = {
        'message': message
    }
    return render(request, 'articles/catch.html', context)

def hello(request, name):
    context = {
        'name': name
    }

    return render(request, 'hello.html', context)