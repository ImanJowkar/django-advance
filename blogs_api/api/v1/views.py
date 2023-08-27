from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from blogs.models import Post
from blogs_api.api.v1.serializers import PostSerializer


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.filter(status=True)
        posts_ser = PostSerializer(posts, many=True)
        return Response(posts_ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_ser = PostSerializer(data=request.data)
        post_ser.is_valid(raise_exception=True)
        return Response(post_ser.data)
#        if post_ser.is_valid():
#            return Response(post_ser.data)
#        else:
#            return Response(post_ser.errors)


class PostDetailView(APIView):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post_ser = PostSerializer(post)
        return Response(post_ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post_ser = PostSerializer(instance=post, data=request.data)
        post_ser.is_valid(raise_exception=True)
        post_ser.save()
        return Response(post_ser.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({"msg": "post sucessfully deleted. "}, status=status.HTTP_204_NO_CONTENT)
