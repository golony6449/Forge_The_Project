from django.shortcuts import render
from blog.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import sessions

# Create your views here.
def index(request):
    list=Context.objects.order_by('postID')
    paraDic={'postList':list}
    temp = list[0].postImage.url
    # print(request.user)
    return render(request, 'blog/index.html',paraDic)

def createPost(request):
    return render(request, 'blog/write.html')

def login(request):
    # print('id',request.POST['id'], 'pass',request.POST['pwd'])
    user=authenticate(request,username=request.POST['id'], password=request.POST['pwd'])

    if user != None:
        # print('success')
        auth_login(request,user)
        return HttpResponseRedirect(reverse('index'))
    else:
        # print('fail')
        # return HttpResponse('로그인 실패 다시시도 해보세요.')
        return HttpResponseRedirect(reverse('index'))

    # return render(request,'blog/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

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

def search(request):
    keyword = request.GET.get('searchKeyword',)
    paraDic={'keyword':keyword}
    return render(request,'test/searchRes.html',paraDic)

def mypage(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        return render(request, 'test/mypage.html')