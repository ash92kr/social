"""social URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),  # 루트 요청이 들어오면 views폴더 안의 HomePage를 view 메소드 활용
    path('accounts/', include('accounts.urls')),   
    path('bye/', views.ByePage.as_view(), name='bye'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('groups/', include('groups.urls')),
    path('posts/', include('posts.urls')),
]
