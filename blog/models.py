from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=200)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    user_id = models.ForeignKey(Profile, related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    body = models.CharField(max_length=500)
    post_id = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)