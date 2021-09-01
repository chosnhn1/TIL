from django.db import models

# Create your models here.
class Article(models.Model):
    # id 생략
    # id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=10) # max_length neccessary > widget class variable 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터 1줄은 인스턴스
    # 클래스 변수로서 선언된 필드 정보
    # cf. instance variable

    