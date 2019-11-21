from rest_framework import serializers
from .models import Profile, Comment, Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(queryset=Profile.objects.all(), slug_field='name')
    
    class Meta:
        model = Post
        fields = ['title', 'body', 'user_id']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Profile
        fields = ['name', 'email', 'address']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body', 'post_id']


class ProfilePostsSerializer(serializers.HyperlinkedModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['name', 'email', 'posts']


class PostCommentsSerializer(serializers.HyperlinkedModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['title', 'body', 'comments']