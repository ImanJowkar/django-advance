from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets
from blogs.models import Post
from blogs_api.api.v1.serializers import PostSerializer


# APIView  ##################################################################################

class PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.filter(status=True)
        posts_ser = self.serializer_class(posts, many=True)
        return Response(posts_ser.data, status=status.HTTP_200_OK)

    def post(self, request):
        post_ser = self.serializer_class(data=request.data)
        post_ser.is_valid(raise_exception=True)
        post_ser.save()
        return Response(post_ser.data)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post_ser = self.serializer_class(post)
        return Response(post_ser.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post_ser = self.serializer_class(instance=post, data=request.data)
        post_ser.is_valid(raise_exception=True)
        post_ser.save()
        return Response(post_ser.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=True)
        post.delete()
        return Response({"msg": "post sucessfully deleted. "}, status=status.HTTP_204_NO_CONTENT)


# Generic ##################################################################################

class PostListGenericApiView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDetailGenericApiView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, *args, **kwargs)

# ViewSets ##################################################################################


class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
