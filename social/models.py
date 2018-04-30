from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    gender=models.CharField(max_length=10,null=True)
    groups=models.ManyToManyField('Group')

class Post(models.Model):
    title = models.CharField(max_length= 50)
    creator=models.OneToOneField(User, on_delete=models.CASCADE)


class Comment(models.Model):
    # Enter info which will be stored in database
    # For Field Types go to https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
    pass

class Group(models.Model):
    users=models.ManyToManyField('UserProfile')
    # Enter info which will be stored in database
    # For Field Types go to https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
    pass

