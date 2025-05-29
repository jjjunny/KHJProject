from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('board.urls')),  # 루트에 board.urls 연결
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/board/', include('board.urls')),   # 기존 API 경로도 유지 가능
    path('api/chat/', include('chat.urls')),
]
