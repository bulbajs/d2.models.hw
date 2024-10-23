from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.IntegerField(default=0)

    def update_rating(self):
        pass


class Category(models.Model):
    category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    NEWS = 'NW'
    ARTICLE = 'AT'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    postType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=128)
    text = models.TextField()
    postRating = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # category = models.ManyToManyField("Category", through="PostCategory")

    def like(self):
        pass

    def dislike(self):
        pass


class Comment(models.Model):
    comment = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    commentRating = models.IntegerField(default=0)

    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
