from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    primaryLanguage = models.CharField(max_length=30)
    name = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.id

class Context(models.Model):
    postID=models.AutoField(primary_key=True)
    postName=models.CharField(max_length=20)
    contents=models.TextField()
    postDate=models.DateTimeField(auto_now_add=True)
    userID=models.CharField(max_length=10)
    postImage=models.ImageField(blank=True)
    postDescription=models.CharField(max_length=15)

    notice=models.CharField(max_length=20, null=True)
    todo1=models.CharField(max_length=20, null=True)
    todo2=models.CharField(max_length=20, null=True)
    todo3=models.CharField(max_length=20, null=True)
    todo4=models.CharField(max_length=20, null=True)
    todo5=models.CharField(max_length=20, null=True)

    def __str__(self):
        return str(self.postID) + '  ' + str(self.postName) + "  " + str(self.postDate)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    field=models.TextField(max_length=20)
    language=models.TextField(max_length=20)

    AUTH_PROFILE_MODULE = 'app.UserProfile'

    # @receiver(post_save, sender=User)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.userprofile.save()