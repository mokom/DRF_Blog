from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detail_create'),
    path('', PostList.as_view(), name='list_create'),
]
