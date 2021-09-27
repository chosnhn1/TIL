from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# 어디서 불러오는지 잘 보시길
from django.views.decorators.http import require_http_methods, require_POST
# 헷갈리는 것 있으면 0916 가서 보시고


# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        # AuthenticationForm 사용법 숙지할 것
        # request 먼저 들어가고 request.POST
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # auth.login 사용법도 숙지할 것
            # 역시 request 먼저 들어가고, form.get_user()로 작성된 폼에서 user 꺼내옴
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        # UserCreationForm 사용법 주의 (Auth Form이랑 다름)
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # UserCreationForm으로 불러왔다면, ModelForm이니까 User를 굳이 import하지 말고 그냥 save해라
            # User 그대로 import: django 비권장사항
            # 폼을 저장하며, 그 내용을 user로 가져와서 로그인 해주기
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
           
    return render(request, 'accounts/signup.html', context)