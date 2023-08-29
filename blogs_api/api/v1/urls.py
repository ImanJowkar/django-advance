from django.urls import path

from blogs_api.api.v1 import views

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='all-post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),

    # generic mixins

    path('generic/posts/', views.PostListGenericApiView.as_view(), name='generic-all-post'),
    path('generic/detail/<int:pk>/', views.PostDetailGenericApiView.as_view(), name='generic-detail-post'),

    # viewsets
    path('viewsets/', views.PostViewSet.as_view(), name='post-list0'),
]

