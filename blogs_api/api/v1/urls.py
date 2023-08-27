from django.urls import path

from blogs_api.api.v1 import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='all-post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]

