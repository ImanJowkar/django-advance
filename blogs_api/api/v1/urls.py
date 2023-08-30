from django.urls import path
from rest_framework.routers import DefaultRouter
from blogs_api.api.v1 import views

router = DefaultRouter()
router.register(r'post-viewset', views.PostModelViewSet, basename='crud-post')
router.register(r'category-viewset', views.CategoryModelViewSet, basename='crud-category')
urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='all-post'),
    path('detail/<int:pk>/', views.PostDetailView.as_view(), name='detail'),

    # generic mixins

    path('generic/posts/', views.PostListGenericApiView.as_view(), name='generic-all-post'),
    path('generic/detail/<int:pk>/', views.PostDetailGenericApiView.as_view(), name='generic-detail-post'),

    # viewsets
]

urlpatterns += router.urls
