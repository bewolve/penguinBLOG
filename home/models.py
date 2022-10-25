from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=120)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article")
    category = models.ManyToManyField(Category, related_name="article")
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(
        upload_to="uploads/articles/",
        null=True,
        default="uploads/articles/noimage.png",
    )
    title = models.CharField(max_length=120)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title[0:50]} - {self.user.username}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title[:30])
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.body[:50]} - {self.user.username}"
