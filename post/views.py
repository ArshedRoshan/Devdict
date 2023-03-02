from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from . serializers import postSerializers,LikeSerializer,questionSerializers,commentSerializers,quelikeSerializers,answerSerializers,questionSaveSerializers,answerlikeSerializer,comment_replySerializers,saveSerializer
from rest_framework.response import Response
from. models import post,Like,question,comment,question_like,answers,answer_like,comment_reply,save_question
from user . serializers import UserSerializers
from rest_framework import generics
from user . models import User
from rest_framework import status
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics
from user . serializers import UserSerializers
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.db.models import F

# Create your views here.

@api_view(['GET','POST'])
def post1(request):
    pserializer = postSerializers(data=request.data,partial=True)
    print('data',request.data)
    if pserializer.is_valid():
        pserializer.save()
    return Response(pserializer.data)


        
    

@api_view(['GET','POST'])   
def postview(request):
    view = post.objects.filter(is_active=1)
    users = User.objects.all()
    serialiazer = UserSerializers(users,many = True)
    return Response(serialiazer.data,200)

@api_view(['GET','POST'])
def admin_post(request):
    paginator = PageNumberPagination()
    paginator.page_size = 4
    pos =    post.objects.all()
    result_page = paginator.paginate_queryset(pos, request)
    
    serializer = postSerializers(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
    


@api_view(['GET','POST'])   
def blockpost(request,id):
    pos = post.objects.filter(id=id)
    print('psss',pos)
    for p in pos:
        if p.is_active == 1:
            p.is_active = 0
            p.save()
            return Response('Block')
        elif p.is_active == 0:
            print('ooooooo',p.is_active)
            p.is_active = 1
            print('kkk',p.is_active)
            p.save()
            return Response('Unblock')
    
        
    
   

class LikeView(APIView):
    def post(self,request,id):
      
        Post = post.objects.get(pk=id)
        user = User.objects.get(username=request.data['use'])
      
        if Like.objects.filter(Post=Post,likeusers=user).exists():
            Like.objects.filter(Post=Post,likeusers=user).delete()
            Post.likes = Post.likes-1
            Post.save()
        else:
            Like.objects.create(Post=Post,likeusers=user)
            Post.likes = Post.likes+1
            Post.save()
        serializer = LikeSerializer(Post,many=True)
        return Response('success')
    
@api_view(['POST'])
def questions(request):
    serializer = questionSaveSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def saved_question(request):
    serializer = saveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,200)
    return Response(serializer.errors)
   
@api_view(['GET','POST'])   
def view_saved(request,id):
    user = User.objects.filter(id=id)
    serializer = UserSerializers(user,many = True)
    return Response(serializer.data) 
 

@api_view(['GET','POST'])   
def questionview(request):
    questions = question.objects.all()
    serialiazer = questionSerializers(questions,many = True)
    return Response(serialiazer.data,200)

@api_view(['GET','POST'])
def questiondetail(request,id):
     questions = question.objects.filter(id=id)
     serialiazer = questionSerializers(questions,many = True)
     return Response(serialiazer.data)
 
 
@api_view(['GET','POST'])
def add_comment(request):
     serializer = commentSerializers(data=request.data,partial = True)
     print('coment',serializer)
     print('valid',serializer.is_valid())
     if serializer.is_valid():
          serializer.save()
     else:
         print(serializer.errors)
     return Response(serializer.data)

@api_view(['GET','POST']) 
def add_reply(request):
    serializer = comment_replySerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response(serializer.errors)
    return Response(serializer.data)
    


@api_view(['GET','POST'])   
def comment_view(request,id):
    Post = post.objects.filter(id=id)
    print('post',Post) 
    serializer = postSerializers(Post,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def like_views(request,id):
    print('requestsss',request)
    post_list = post.objects.filter(pk=id)
    print('post_lis',post_list.user)
    like_count = Like.objects.filter(Post=id).count()
    print('count',like_count)
    post_serializer = postSerializers(post_list,many=True,context={"like_count":like_count})
    return Response(post_serializer.data)
    
# @api_view(['GET','POST'])
# def question_likes(request,id):
#     request.data = 1
#     print('request',request.data['use'])
#     Question = question.objects.get(pk=id)
#     user = User.objects.get(username=request.data['use'])
#     print('user',user)
#     print('Post',Question)
#     if question_like.objects.filter(Question=Question,likeusers=user).exists():
#         question_like.objects.filter(Question=Question,likeusers=user).delete()
#         Question.likes = Question.likes-1
#         Question.save()
#     else:
#         question_like.objects.create(Questiont=Question,likeusers=user)
#         Question.likes = Question.likes+1
#         Question.save()
#     serializer = quelikeSerializers(Question,many=True)
#     return Response('success')     

class question_likes(APIView):
    def post(self,request,id):
        print('request',request.data['use'])
        Question = question.objects.get(pk=id)
        user = User.objects.get(username=request.data['use'])
        print('user',user)
        print('Question',Question)
        if question_like.objects.filter(Question=Question,likeusers=user).exists():
             pass
        else:
            question_like.objects.create(Question=Question,likeusers=user)
            Question.like = Question.like+1
            Question.save()
        serializer = LikeSerializer(Question,many=True)
        return Response('success')
    
class dislike(APIView):
    def post(self,request,id):
        print('request',request.data['use'])
        Question = question.objects.get(pk=id)
        user = User.objects.get(username=request.data['use'])
        print('user',user)
        print('Question',Question)    
        if question_like.objects.filter(Question=Question,likeusers=user).exists():
            question_like.objects.filter(Question=Question,likeusers=user).delete()
            Question.like = Question.like-1
            Question.save()
    
        serializer = LikeSerializer(Question,many=True)
        return Response('dislike success')
    
    
@api_view(['GET','POST'])
def answers_to(request):
     print('request',request)
     serializer = answerSerializers(data=request.data)
     print('data',request.data)
     print('seriaizer',serializer)
     print('valid',serializer.is_valid())
     print('error',serializer.errors)
     if serializer.is_valid():
          print('error',serializer.errors)
          serializer.save()
     return Response(serializer.data)
 
@api_view(['GET','POST'])   
def answer_view(request,id):
    Question = question.objects.filter(id=id)
    print('post',Question) 
    serializer = questionSerializers(Question,many=True)
    return Response(serializer.data)

class answer_likesss(APIView):
    def post(self,request,id):
        print('request',request.data['use'])
        answer = answers.objects.get(id=id)
        user = User.objects.get(username=request.data['use'])
        print('user',user)
        print('answer',answer)
        if answer_like.objects.filter(Answer=answer,liked_by=user).exists():
              pass
        else:
            answer_like.objects.create(Answer=answer,liked_by=user)
            answer.like = answer.like+1
            answer.save()
        serializer =answerlikeSerializer(answer,many=True)
        return Response('success')
    

class answer_dislike(APIView):
    def post(self,request,id):
        print('request',request.data['use'])
        answer = answers.objects.get(pk=id)
        user = User.objects.get(username=request.data['use'])
        print('user',user)
        print('answer',answer)    
        if answer_like.objects.filter(Answer=answer,liked_by=user).exists():
            answer_like.objects.filter(Answer=answer,liked_by=user).delete()
            answer.like = answer.like-1
            answer.save()
    
        serializer = answerlikeSerializer(answer,many=True)
        return Response('dislike success')
    
@api_view(['GET','POST'])
def postcount(request):
    a = []
    p = post.objects.filter(is_active = 1).count()
    a.append(p)
    print('aaaaa',a)
    return Response(a)

@api_view(['GET','POST'])
def questioncount(request):
    b = []
    q = question.objects.all().count()
    b.append(q)
    return Response(b)

@api_view(['GET','POST'])
def popularposts(request):
    a = []
    b=[]
    posts = post.objects.filter(likes__gt = 2)
    for i in posts:
        z = i.likes
        a.append(z)
    print('aaa',a)
    p = post.objects.filter(likes__gt = 2)
    for i in p:
        z = i.caption
        b.append(z)
    print('bbbb',b)
    return Response({'a':a,'b':b})
    
   
        