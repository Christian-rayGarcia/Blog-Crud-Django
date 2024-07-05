from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
	title = models.CharField(max_length=250)
	excerpt = models.TextField(null=True)
	content = models.TextField()
	slug = models.SlugField(max_length=250, unique_for_date='published')
	published = models.DateTimeField(default=timezone.now)
