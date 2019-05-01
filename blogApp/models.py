from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	category_name = models.CharField(max_length=50)
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.category_name


class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	category = models.ForeignKey(Category, on_delete=models.SET_NULL,blank=True,null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	post_thum = models.ImageField(upload_to='post',null = True,blank=True)

	def __str__(self):
		return self.title
# Create your models here.
