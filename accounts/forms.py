from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserCreateForm(UserCreationForm):  # UserCreationForm을 상속받음
    
    class Meta:
        # fields = '__all__'
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()  # user 모델을 가져와서 값을 입력함