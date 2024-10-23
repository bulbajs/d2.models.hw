from django.db import models
# from django.contrib.auth import base_user


class Author(models.Model):
    rating = models.FloatField(default=0.0)
    author = models.CharField(max_length=255)
    # user = models.OneToOneField("AbstractUser", on_delete=models.CASCADE)


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    post = models.BooleanField(default=False)
    title = models.TextField()
    text = models.TextField()
    post_rating = models.FloatField(default=0.0)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", through="PostCategory")


class Comment(models.Model):
    comment = models.TextField()
    comment_time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)

    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
