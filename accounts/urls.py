from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # 위의 이름과 동일함(외부 폴더이므로 이름을 바꿈)

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),    
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),   # class 실행하기 위해 as_view를 사용함
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]


