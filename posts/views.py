from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Post
from groups.models import GroupMember
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
class PostList(ListView):
    model = Post

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'message', 'group')  # 사용자가 입력할 수 있는 부분만 적는다

    def form_valid(self, form):  # 로그인한 사람만 유저 정보에 들어가도록 설정
        self.object = form.save(commit=False)  
        self.object.user = self.request.user   # 유저 정보만 끼워 넣음
        self.object.save()
        
        return super().form_valid(form)
        
class PostDetail(DetailView):
    model = Post

class UserPosts(ListView):  # 모델 이름_리스트_테이블 이름 정렬
    model = Post
    tempate_name = 'posts/user_post_list.html'  # 위와 중복되므로 변경
    
    def get_queryset(self):  # 자기가 알아서 자동으로 get, post로 보냄
        try:  # 유저와 posts 라이브러리가 연결되어 있음
            # self.post_user = User.objects.prefetch_related('posts').get(조건)
            # self.post_user = User.objects.prefetch_related('posts').get(username=self.kwargs.get('username'))
              self.post_user = User.objects.prefetch_related('post_set').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:  # 유저가 없다
            raise Http404
        else:
            return self.post_user.posts.all  # 모든 post가 포함될 있음
            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user']  = self.post_user # 위의 것을 가져옴
        return context 
    
     
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('posts:list')  # 성공했을 때 이동할 url
    
    def get_queryset(self):   # 특정 User가 만든 쿼리셋 찾아 본인이 아니면 수정 못하게 막기
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)  # 로그인한 user와 글을 쓴 user가 다르면 아무 버튼도 나오지 않음
    
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('message',)
    
    def get_queryset(self):   # 특정 User가 만든 쿼리셋 찾아 본인이 아니면 수정 못하게 막기
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)  # 로그인한 user와 글을 쓴 user가 다르면 아무 버튼도 나오지 않음
    
    