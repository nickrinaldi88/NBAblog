from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'post_type', 'root_url', 'html', 'created_at')
    # take model
    # translate into json response


class CreatePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_type', 'root_url', 'html', 'created_at')
 
