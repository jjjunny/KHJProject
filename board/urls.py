from django.urls import path
from .views import PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    # 필요하다면 추가로 detail, create 등 다른 패턴도 여기에 작성
]
