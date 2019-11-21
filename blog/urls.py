from django.urls import path
from blog import views


urlpatterns = [
    path('profiles', views.ProfileList.as_view(), name=views.ProfileList.name),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('posts', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('comments', views.CommentList.as_view(), name=views.CommentList.name),
    path('profile-posts', views.ProfilePostsList.as_view(), name=views.ProfilePostsList.name),
    path('post-comments', views.PostCommentsList.as_view(), name=views.PostCommentsList.name),
    path('post/<int:pk_post>/comment/<int:pk_comment>/', views.PostSpecificCommentList.as_view(), name=views.PostSpecificCommentList.name),
]