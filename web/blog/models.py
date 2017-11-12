from django.db import models
from django.utils.timezone import now

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
    toDo=models.TextField()

    def __str__(self):
        return str(self.postName) + "    " + str(self.postDate)