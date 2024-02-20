"""
URL configuration for turtorialdjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
# views 접두사를 제거한 상태로 뷰 함수를 직접 임포트합니다.
from main.views import about, notice_list, notice_detail_1, notice_detail_2, notice_detail_3, contact, abcde, user_hojun, user_mini

urlpatterns = [
    path('about/', about, name='about'),  # views 접두사 제거
    path('notice/', notice_list, name='notice_list'),  # views 접두사 제거
    path('notice/1', notice_detail_1, name='notice_detail_1'),  # views 접두사 제거
    path('notice/2', notice_detail_2, name='notice_detail_2'),  # views 접두사 제거
    path('notice/3', notice_detail_3, name='notice_detail_3'),  # views 접두사 제거
    path('contact/', contact, name='contact'),  # views 접두사 제거
    path('a/b/c/d/', abcde, name='abcde'),  # views 접두사 제거
    path('user/hojun', user_hojun, name='user_hojun'),  # views 접두사 제거
    path('user/mini', user_mini, name='user_mini'),  # views 접두사 제거
]
