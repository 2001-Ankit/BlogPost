from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import AbstractUser, Group, Permission, User
from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=400)
    avatar = models.ImageField(upload_to='media/')
    email = models.EmailField(blank=False)
    status = models.CharField(max_length=400)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    permissions = models.ManyToManyField(Permission)
    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    roles = models.ManyToManyField(Role)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=400)
    slug = models.SlugField(blank=True,unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(blank=True,unique=True)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="blogposts")


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


from django.db import models
from .models import Category

class Permission(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.category.name