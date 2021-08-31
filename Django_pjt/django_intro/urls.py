"""django_intro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# from articles import views

urlpatterns = [
    # path('index/', views.index),
    # path('introduce/', views.introduce),
    # path('greeting/', views.greeting),
    # path('dinner/', views.dinner),
    # path('image/', views.image),
    # path('template_language/', views.template_language),
    # path('throw/', views.throw),
    # path('catch/', views.catch),
    # path('hello/<name>/', views.hello),
    path('articles/', include('articles.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),

    
]
