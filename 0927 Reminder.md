# 0927 Reminder

static

settings에서는

STATIC_URL = '/static/'

STATICFILES_DIRS = [ BASE_DIR / 'static', ]



media를 가져다 쓰고 싶다면

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'

urls에서

from django.conf.urls.static import static

urlpatterns에

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



template에서는

load static 해서 쓸 수 있도록...!

static '파일 위치'





login

함수, 폼 등 사용법 체크

AuthenticationForm(request, request.POST)

얘는 첫번째 인자로 무조건 request 가져가기



UserCreationForm(request.POST)

글을 작성할 때 이렇게 받았었지?

form = ArticleForm(request.POST)

수정할 때는 어떻게?

article = Article.objects.... (DB에서 가져오고)

form = ArticleForm(request.POST, instance=article)



User도 기본적으로 비슷하다

회원가입, 수정, 삭제는 거의 똑같고 (다만 무슨 Model, Form을 쓰느냐 문제)

Login Logout은 Auth가 구현해준 것을 쓰면서

User 대신 Session을 만드는 구조



@require_POST & @login_required 데코레이터를 함께 쓰면 안 되는 문제 (login_required가 로그인 후 접속할 URL을 get으로 던지므로 발생)

: @login_required 대신 request.user.is_authenticated을 확인하자.



@login_require가 만드는 get을 이용하는 법

login 정의 시에 어디로 리다이렉트할 것인가에서 python의 Boolean 평가를 이용

return redirect(request.GET.get('next') or 'articles:index')

