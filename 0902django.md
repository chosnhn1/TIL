admin page

```
python manage.py createsuperuser
>>> 사용자 이름
>>> 이메일 주소 (not necessary)
>>> Password:
```



admin에 model 등록

admin.py

```python
from .models import Article

admin.site.register(Article)
# admin.site.register(Model명)
```



관리자 사이트에 표시되는 형식은?

def \__str__(self)



admin.py

```python
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')
```

