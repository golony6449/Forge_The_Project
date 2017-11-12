from django.shortcuts import render
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    list=Context.objects.order_by('postID')
    paraDic={'postList':list}
    return render(request, 'blog/index.html',paraDic)

def createPost(request):
    return render(request, 'blog/write.html')

def login(request):
    # id(이메일), pwd
    print('id',request.POST['id'], 'pass',request.POST['pwd'])
    user=authenticate(username=request.POST['id'], password=request.POST['pwd'])

    if user != None:
        print('success')
        return HttpResponseRedirect(reverse('index'))
    else:
        print('fail')
        return HttpResponseRedirect(reverse('register'))

    # return render(request,'blog/login.html')

def write(request):
    return render(request,'test/write.html')

def regpost(request):
    newPost=Context(postName=request.POST['title'],contents=request.POST['contents'],
                    toDo=request.POST['contents'], userID='temp')
    newPost.save()

    return HttpResponseRedirect('/')

def register(request):
    return render(request,'test/register.html',)

def reguser(request):
    newUser=User.objects.create_user(request.POST['id'],request.POST['email'],request.POST['pwd'])
    newUser.save()

    return HttpResponseRedirect(reverse('index'))

def viewPost(request,post_id):
    obj=Context.objects.get(postID=post_id)
    text=obj.contents

    return render(request, 'test/post.html',{'title':obj.postName ,'contents':text, 'id':obj.postID,
                                             'author':obj.userID,'when':obj.postDate})