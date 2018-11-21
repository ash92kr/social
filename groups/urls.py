from django.urls import path
from . import views

app_name = 'groups'

urlpatterns = [
    path('', views.GroupList.as_view(), name='list'),   # 그룹에 대한 반환 요청을 받아 그룹 테이블에 있는 그룹 이름을 리스트로 나열
    path('create/', views.GroupCreate.as_view(), name='create'),
    path('posts/in/<slug>', views.GroupDetail.as_view(), name="detail"),  # slug는 일종의 id값으로 이해하면 됨
    path('join/<slug>', views.GroupJoin.as_view(), name='join'),
    path('leave/<slug>', views.GroupLeave.as_view(), name='leave'),
]