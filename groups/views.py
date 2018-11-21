from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, RedirectView
from .models import Group, GroupMember
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
class GroupList(ListView): # 쿼리 기반 
    model = Group

class GroupCreate(CreateView, LoginRequiredMixin):
    model = Group
    fields = ('name', 'description')
    # login을 하지 않으면 creategroup 버튼이 나오지도 않으며 groups/create를 입력해도 그룹 만들지 못하게 로그인 필수

class GroupDetail(DetailView):
    model = Group
    
    
class GroupJoin(LoginRequiredMixin, RedirectView):
    # 코드 실행 후 리다이렉트 할 주소 설정
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug':self.kwargs.get('slug')})
        
    # 코드 실행
    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.group('slug'))
        
        
        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        
        except IntegrityError:  # 에러 시 대처
            messages.warning(self.request, 'already a member')
        
        else:
            messages.success(self.request, 'add a new member')
            
        return super().get(request, *args, **kwargs)
    
class GroupLeave(LoginRequiredMixin, RedirectView):
    # 코드 실행 후 리다이렉트 할 주소 설정
    def get_redirect_url(self, *args, **kwargs):
        return reverse('groups:detail', kwargs={'slug':self.kwargs.get('slug')})
        
    def get(self, request, *args, **kwargs):
        try:
            membership = GroupMember.objects.filter(
                user = self.request.user,
                group__sulg = self.kwargs.get('slug').get())
        
        except GroupMember.DoesNotExist:
            messages.warning(self.request, 'sorry')
        
        else:
            membership.delete()
            messages.success(self.request, 'delete!!')
        
        return super().get(request, *args, **kwargs)
        