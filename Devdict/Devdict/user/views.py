import uuid
from django.shortcuts import render
from .serializers import UserSerializers,followSerialiazers,profileSerializers,applicationSerializers,follow1Serialiazers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from . models import User,follow,Application
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import generics
from django.urls import reverse
from django.core.mail import EmailMessage
# from .utils import Util
import jwt
from django.conf import settings
# from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from user.tasks import celeryusing
from rest_framework.pagination import PageNumberPagination
# Create your views here.

@api_view(['GET','POST'])
def signup(request):
     print('request',request)
     user = request.data
     serializer = UserSerializers(data=request.data,partial=True)
     print('data',request.data)
    
     if serializer.is_valid() :
        print('errorr',serializer.errors)
        serializer.save()
        print('uyuyu',user['email'],user['username'])
        celeryusing.delay(user['email'],user['username'])
        return Response(200)
     return Response(serializer.errors)



    
@api_view(['GET','POST']) 
def validate(request):
    token = request.data['id']
    username = request.data['username']
    if token is not None:
        ts = User.objects.get(username = username)
        ts.is_verfied = True
        ts.save()
        return Response(200) 
    else:
        return Response(400)
 

    

# @api_view(['GET','POST'])
# def getss(request):
#         token = request.data('token')
#         print('to',token)
#         try:
#             payload = jwt.decode(token,settings.SECRET_KEY)
#             print('payload',payload)
#             user = User.objects.get(id=payload['user_id'])
#             if not user.is_verfied:
#                 user.is_verfied = True
#                 user.save()
#                 return Response({'email':'successfully Activated'},200)
#         except jwt.ExpiredSignatureError as identifier:
#             return Response({'error':'Link expired'},400)  
#         except jwt.exceptions.DecodeError as identifier:
#             return Response('Invalid token',400) 
        

@api_view(['GET','POST'])
def add_dp(request):
    print('dataa1',request.data)
    serialaizer = profileSerializers(data=request.data)
    print('ssss',serialaizer)
    print(serialaizer.is_valid())
    if serialaizer.is_valid():
        print('error',serialaizer.errors)
        serialaizer.save()
    return Response(serialaizer.data)

@api_view(['GET','POST'])       
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh'
    ]  
    
    return Response(routes)

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['company_name'] = user.company_name
        token['Account_type'] = user.Account_type
        token['first_name'] = user.first_name
        token['is_admin'] = user.is_admin
        token['is_active'] = user.is_active
        token['is_block'] = user.is_block
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    

@api_view(['GET','POST']) 
def user_list(request):
    users = User.objects.filter().order_by('id')[:5]
    serialiazer = UserSerializers(users,many = True)
    return Response(serialiazer.data,200,users)

# @api_view(['GET','POST']) 
# def user_follow(request):
#     pass
    
    
@api_view(['GET','POST'])
def follows(request):
    follower_username = request.data.get('follower_username')
    following_username = request.data.get('following_username')
    follower = User.objects.get(username=follower_username)
    following = User.objects.get(username=following_username)
    if follow.objects.filter(follower=follower, following=following).exists():
        follow.objects.filter(follower=follower, following=following).delete()
        if following.follower > 0  :
            following.follower = following.follower-1
            follower.follow = follower.follow-1
            following.is_follower = False
            follower.is_follow = False
        following.save()
        follower.save()
        following = User.objects.filter(username=following_username)
        serializer = UserSerializers(following,many = True)
        return Response(serializer.data)
    else:
        follow.objects.create(follower=follower, following=following)
        following.follower = following.follower+1
        follower.follow =  follower.follow+1
        following.is_follower = True
        follower.is_follow = True
        follower.save()
        following.save()
        following = User.objects.filter(username=following_username)
        serializer = UserSerializers(following,many = True)
        return Response(serializer.data)
        

# @api_view(['GET','POST'])
# def unfollow(request):
#         follower_username = request.data.get('follower_username')
#         following_username = request.data.get('following_username')
#         follower = User.objects.get(username=follower_username)
#         following = User.objects.get(username=following_username)
#         Follow = follow.objects.get(follower=follower, following=following)
#         Follow.delete()
#         return Response('success')
    
@api_view(['GET','POST'])   
def follow_check(request):
    print('req',request.data)
    check = follow.objects.filter(follower= request.data['follower'],following=request.data['following'])
    print('check',check)
    if check:
        return Response('following')
    else:
        return Response('follow')
    
    
    
@api_view(['GET','POST']) 
def company_list(request):
    users = User.objects.filter(Account_type='company')
    serialiazer = UserSerializers(users,many = True)
    return Response(serialiazer.data,200)

@api_view(['GET','POST'])   
def my_profile(request,id):
    users = User.objects.filter(pk=id)
    serialiazer = UserSerializers(users,many = True)
    return Response(serialiazer.data,200)
    
    
@api_view(['GET','POST'])   
def application(request):
    print('request',request.data)
    serializer = applicationSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return Response(serializer.errors)
 
# @api_view(['GET','POST'])       
# def applicant_view(request,id):
#     app = Application.objects.filter(processing=False,Accept=False,Decline=False,id=id)
#     print('appp',app)
#     # user = User.objects.filter(id=id)
#     serializer = applicationSerializers(app,many=True)
#     print('app ser',serializer.data)
#     return Response(serializer.data)

@api_view(['GET','POST'])       
def applicant_view(request,id):
    app = Application.objects.filter(processing=False,Accept=False,Decline=False,company_name=id)
    seraialiazer = applicationSerializers(app,many=True)
    return Response(seraialiazer.data)

@api_view(['GET','POST']) 
def process_list(request,id,cid):
    app = Application.objects.filter(processing=False,Accept=False,Decline=False,id=id)
    print('apppp',app)
    app.update(processing=True)
    apps = Application.objects.filter(processing=False,company_name=cid)
    print('update',apps)
    seraialiazer = applicationSerializers(apps,many=True)
    return Response(seraialiazer.data)

@api_view(['GET','POST'])
def process_list1(request,id):
    app = Application.objects.filter(processing=True,Accept=False,Decline=False,company_name=id)
    seraialiazer = applicationSerializers(app,many=True)
    print('processlist1',seraialiazer.data)
    return Response(seraialiazer.data)

@api_view(['GET','POST'])
def accept(request,id,cid):
    app = Application.objects.filter(processing=True,Accept=False,Decline=False,id=id)
    print('apppp',app)
    app.update(Accept=True)
    apps = Application.objects.filter(processing=True,Accept=False,company_name=cid)
    seraialiazer = applicationSerializers(apps,many=True)
    return Response(seraialiazer.data)

@api_view(['GET','POST'])
def accept1(request,id):
    app = Application.objects.filter(processing=True,Accept=True,Decline=False,company_name=id)
    seraialiazer = applicationSerializers(app,many=True)
    return Response(seraialiazer.data)


@api_view(['GET','POST'])
def application_status(request,id): 
    user = User.objects.filter(id=id)  
    serializer = UserSerializers(user,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def sendmail(request):
    pass

@api_view(['GET','POST'])
def chat_users(request):
    fooo = follow.objects.all()
    print('chaa',fooo)
    serializer = follow1Serialiazers(fooo,many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def admin_user(request):
    # paginator = PageNumberPagination()
    # paginator.page_size = 4
    user = User.objects.filter(Account_type = 'personal')
    # result_page = paginator.paginate_queryset(user, request)
    serializer = UserSerializers(user,many = True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def admin_comp(request):
    user = User.objects.filter(Account_type = 'company')
    serializer = UserSerializers(user,many = True)
    return Response(serializer.data)
 

@api_view(['GET','POST'])
def block_user(request,id):
    user = User.objects.get(id=id)
    if user.is_active == True:
        user.is_active = False
        user.save()
        return Response('Block')
    elif user.is_active == False:
        print('ooooooo',user.is_active)
        user.is_active = True
        print('kkk',user.is_active)
        user.save()
        return Response('Unblock')

@api_view(['GET','POST'])
def count(request):
    a = []
    b = []
    user = User.objects.all()
    for i in user:
        z = i.id
    personal = User.objects.filter(Account_type = 'personal').count()
    a.append(personal)
    company = User.objects.filter(Account_type = 'company').count()
    a.append(company)
    return Response(a)

#  a = []
#         b = []
#         graph = product.objects.all()
#         for i in graph:
#            z=i.id
#            count = OrderProduct.objects.filter(Product=z).count()
#            a.append(i.productname)
#            b.append(count)
    
    