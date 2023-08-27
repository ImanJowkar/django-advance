from rest_framework import serializers
from blogs.models import Post


# class PostSerializer(serializers.Serializer):
#    id = serializers.IntegerField()
#    image = serializers.ImageField()
#    title = serializers.CharField(max_length=255)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'status', 'published_at']
