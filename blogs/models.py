from django.db import models
from accounts.models import User


# Create your models here.


class Post(models.Model):
    """
    This is Post model for defining the fields of Post model.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='blogs/')
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
