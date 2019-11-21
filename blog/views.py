from django.shortcuts import render
from rest_framework import status, generics

from .models import Profile, Post, Comment
from .serializers import ProfileSerializer, PostSerializer, CommentSerializer, ProfilePostsSerializer, PostCommentsSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profiles'


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'posts'


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comments'


class ProfilePostsList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilePostsSerializer
    name = 'profile-posts' 


class PostCommentsList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCommentsSerializer
    name = 'post-comments'


class PostSpecificCommentList(generics.ListCreateAPIView):
    serializer_class = PostCommentsSerializer
    name = 'post-specific-comment'

    def get_queryset(self):
        param = self.request.query_params.get('pk_post', None)
        print(self.request.query_params)
        print(param)
