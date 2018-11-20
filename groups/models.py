from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)  # 같은 이름의 그룹은 생성불가
    slug = models.SlugField(allow_unicode=True, unique=True)  # 띄어쓰기 대신 -로 문자를 묶음 -> 그룹 이름을 url에 포함하기
    description = models.TextField()
    members = models.ManyToManyField(User, through='GroupMember')  # accounts 모델을 추가해서 넣거나 get_user_model을 넣는다(일대다 관계 연결)
    # GroupMember가 조인 테이블이 됨(User와 Group에 동일한 사람들이 여러 곳에 속할 수 있기 때문)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):  # 자동으로 위에 입력한 내용을 입력하면
        # 첫 번째는 지금 입력한 값, 두 번째는 kev-value 값을 받는다
        self.slug = slugify(self.name)  # 사용자가 입력한 이름을 슬러그 값으로 바꿈
        super().save(*args, **kwargs)  # 부모가 가진 값도 저장함
        
    def get_absolute_url(self):
        return reverse('groups:detail', kwargs={'slug':self.slug})
        # 그룹의 이름을 url에 넣음
        
    class Meta :
        ordering = ['name']  # 그냥 넣으면 상향식, -name으로 하면 하향식
    
class GroupMember(models.Model):  # User와 group이라는 두 개의 컬럼이 존재
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # CASCADE 속성은 하나가 지워지면 다른 하나도 지워진다는 뜻
    
    def __str__(self):
        return self.user.username
        
    class Meta:
        unique_together = ('group', 'user')  # group명은 하나만 가질 수 있다