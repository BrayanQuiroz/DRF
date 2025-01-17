from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=10, choices=options, default='published')
    object = models.Manager()
    post_objects = PostObjects()

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.title
