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
    # temp = list[0].postImage.url
    # print(request.user)
    return render(request, 'blog/index.html',paraDic)

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
        paraDic={'errCode': 4}
        return render(request, 'test/error.html', paraDic)

    # return render(request,'blog/login.html')

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('index'))

def write(request):
    if not request.user.is_authenticated():
        paraDic={'errCode': 2}
        return render(request,'test/error.html', paraDic)

    paraDic={'post':None, 'edit':False}
    return render(request,'blog/write.html', paraDic)

def regpost(request, post_id=-1):
    if not request.user.is_authenticated():
        paraDic={'errCode': 2}
        return render(request,'test/error.html', paraDic)

    if post_id==-1:     ## 작성
        Post = Context(postName=request.POST['title'],contents=request.POST['contents'], userID=request.user,
                      postDescription=request.POST['description'], postImage=request.FILES['image'])
        print(request.FILES)


        Post.todo1=None
        Post.todo2=None
        Post.todo3=None
        Post.todo4=None
        Post.todo5=None
        Post.notice=None

        Post.recentChangedBy = request.user.username
        Post.recentChangedTitle = 'New project Created'
        Post.recentChangedDescription = "Let's do something NEW"

        Post.save()
    else:       ## 수정
        Post=Context.objects.get(postID=post_id)
        # Post.postName=request.POST['title']
        Post.contents=request.POST['contents']
        Post.postDescription=request.POST['description']
        Post.todo1=request.POST['todo1']
        Post.todo2=request.POST['todo2']
        Post.todo3=request.POST['todo3']
        Post.todo4=request.POST['todo4']
        Post.todo5=request.POST['todo5']
        Post.notice=request.POST['notice']
        Post.recentChangedBy = request.user.username
        Post.recentChangedTitle = 'edit Something'
        Post.recentChangedDescription = "Please Check Changelog"

        Post.save()

    return HttpResponseRedirect('/detail/'+str(Post.postID))

def register(request):
    return render(request,'test/register.html',)

def reguser(request):
    print(request.POST['regid'])
    paraDic = {'username': request.POST['firstName'] + request.POST['lastName'], 'errCode': 3}
    try:
        newUser = User.objects.create_user(request.POST['regid'], request.POST['email'], request.POST['regpwd'])
        newUser.first_name = request.POST['firstName']
        newUser.last_name = request.POST['lastName']
        # newUser.profile.field=request.POST['field']
        # newUser.profile.laguage=request.POST['language']

        newUser.save()
        return render(request,'test/welcome.html', paraDic)
    except:
        return render(request,'test/error.html', paraDic)

def viewPost(request,post_id):
    obj=Context.objects.get(postID=post_id)

    paraDic = {'title':obj.postName ,'contents':obj.contents, 'id':obj.postID,
               'author':obj.userID,'when':obj.postDate, 'path':obj.postImage}

    return render(request, 'test/post.html', paraDic)

def search(request):
    keyword = request.GET.get('searchKeyword',)
    result=Context.objects.filter(postName__regex=r'.*'+keyword+'.*')
    print(result)
    if result.exists():
        paraDic={'keyword':keyword, 'resList':result}
        print('exist')
    else:
        paraDic={'keyword':keyword, 'resList':None}

    return render(request,'blog/searchRes.html',paraDic)

def mypage(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/')
    # else:
        paraDic={'user':request.user, 'userData':User.objects.get(username=request.user)}
        return render(request, 'test/mypage.html',paraDic)

def welcome(request):
    paraDic={'username':11}
    return render(request,'test/welcome.html', paraDic)

def error(request):
    paraDic={}
    return render(request, 'test/error.html', paraDic)

def detail(request,post_id):
    if not request.user.is_authenticated:
        paraDic={'errCode': 2}
        return render(request,'test/error.html', paraDic)

    obj=Context.objects.get(postID=post_id)

    total=5

    paraDic={'post':obj, 'value1':3,'value2':6}
    return render(request, 'blog/project.html',paraDic)

def edit(request, post_id):
    obj=Context.objects.get(postID=post_id)

    paraDic={'post':obj, 'edit':True}

    return render(request, 'blog/write.html', paraDic)

# TODO: 프로젝트 페이지의 참여중인 사용자명 수정
def join(request, post_id):
    error = False
    obj=Context.objects.get(postID=post_id)
    if obj.member1 is None:
        obj.member1=request.user.username
        obj.recentChangedBy = request.user.username
        obj.recentChangedTitle = request.user.username + ' joined'
        obj.recentChangedDescription = 'New people participated'
        obj.save()


    elif obj.member2 is None:
        obj.member2=request.user.username
        obj.recentChangedBy = request.user.username
        obj.recentChangedTitle = request.user.username + ' joined'
        obj.recentChangedDescription = 'New people participated'
        obj.save()
    else:
        paraDic = {'errCode': 1}
        error = True

    #TODO: 슬롯이 다 찬 경우 예외처리 (에러페이지로 리다이렉트)

    if error == False:
        return HttpResponseRedirect('/detail/' + str(post_id))
    else:
        return render(request, 'test/error.html', paraDic)

def quit(request, post_id):
    obj=Context.objects.get(postID=post_id)
    if obj.member1==request.user.username:
        obj.member1=None
        obj.recentChangedBy = request.user.username
        obj.recentChangedTitle = request.user.username + ' quit this Project'
        obj.recentChangedDescription = 'Sayonara'
        obj.save()
    elif obj.member2==request.user.username:
        obj.member2=None
        obj.recentChangedBy = request.user.username
        obj.recentChangedTitle = request.user.username + ' quit this Project'
        obj.recentChangedDescription = 'Sayonara'
        obj.save()

    return HttpResponseRedirect('/detail/'+str(post_id))

def game(request):
    return render(request,'blog/game.html')