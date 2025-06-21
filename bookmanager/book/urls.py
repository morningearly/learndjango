from django.urls import path
from book.views import index

urlpatterns = [
    # 路由 函数
    path('index/', index)
]
