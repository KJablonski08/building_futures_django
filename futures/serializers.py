from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'body', 'post', 'timestamp', 'author')


class PostSerializer(serializers.ModelSerializer):
    posts = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'updated', 'timestamp', 'posts')
