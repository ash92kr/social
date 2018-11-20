from django.db import models
from django.contrib import auth

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):  # 기본적으로 장고가 가진 user를 상속받아 User에 그대로 넣음
    def __str__(self):
        return "@{}".format(self.username)
        # @username으로 출력됨