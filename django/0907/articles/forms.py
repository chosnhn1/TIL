from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        # metadata for form
        model = Article
        fields = '__all__'
        # recommend: clarify fields
        # fields = ['title', 'content']
        #### Python 문법 주의
        # when use tuple, ',' is mandatory