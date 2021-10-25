# Entity-Relationship Diagram: ERD

개체-관계 모델

자료의 구조화



## Crow's Foot

Oracle에서 사용하는 Notation





----

Memo



그때그때 _set 계산말고

annotate하면 좋을 것 (최적화)



```python
reviews = Review.objects.annotate(Count('comment'))
reviews = Review.objects.annotate(comment__count=Count('comment'))

reviews = Review.objects.select_related('author')
# inner join





r.comment__count
```



