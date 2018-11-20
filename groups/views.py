from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Group
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class GroupList(ListView):
    model = Group

class GroupCreate(CreateView, LoginRequiredMixin):
    model = Group
    fields = ('name', 'description')
    # login을 하지 않으면 creategroup 버튼이 나오지도 않으며 groups/create를 입력해도 그룹 만들지 못하게 로그인 필수

class GroupDetail(DetailView):
    model = Group