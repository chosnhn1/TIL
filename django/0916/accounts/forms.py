from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
# why get_user?
# many apps: select user model

User = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', )