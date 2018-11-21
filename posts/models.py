from django.db import models
from groups.models import Group
from django.contrib.auth import get_user_model

User=get_user_model()

from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={
                        'username' : self.user.username,
                        'pk' : self.pk
        })
        
    class Meta:
        ordering = ['-created_at']  # 최신글이 가장 위로 올라오도록 역순으로 지정
        