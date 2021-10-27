# DRF w/ 1:N Relation

2개 이상의 1:N 관계를 갖는 모델을 DRF로 구현하기



0. DB 초기화

1. models.py에서 1:N 모델 Comment 작성

2. Comment에 대응하는 Serializer 작성

3. 사용

   * 단, 어떤 1을 참조하는지에 대한 정보가 필요 (외래 키)

   * 입력을 받는 것이 아닌, URL을 통해 자동으로 가져오게 됨

   * Read Only Field

   * ```python
     class Meta:
         model = Comment
         fields = '__all__'
         read_only_fields = ('article',)
     ```



* 특정 게시글의 댓글 출력하기
  * Primary Key Related Field (역참조 들고 오기)
    * `serializers.PrimaryKeyRelatedField()`
  * Nested Relationships
* 개수 구하기
  * `source` argument



----

drf-yasg, swagger

코드 변경 시 명세 자동 연동