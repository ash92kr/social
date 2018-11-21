from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),   # post를 받을 수 있는 path를 열어 놓음
    path('create/', views.PostCreate.as_view(), name='create'),   # 게시글 쓰기
    path('by/<username>/<pk>/', views.PostDetail.as_view(), name='detail'),  # user가 작성한 글만 보여주기
    path('by/<username>/', views.UserPosts.as_view(), name='for_user'),
    path('delete/<pk>', views.PostDelete.as_view(), name='delete'),  # 글 삭제하기
    path('update/<pk>', views.PostUpdate.as_view(), name='update'),  # 글 수정하기
]
