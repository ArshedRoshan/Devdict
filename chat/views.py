from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ChatRoomSerializer, ChatMessageSerializer
from .models import ChatRoom, ChatMessage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import User

# Create your views here.
def chat(request):
    pass

# class ChatRoomViewSet(viewsets.ModelViewSet):
#     queryset = ChatRoom.objects.all()
#     serializer_class = ChatRoomSerializer
    
# class ChatMessageViewSet(viewsets.ModelViewSet):
#     queryset = ChatMessage.objects.all()
#     serializer_class = ChatMessageSerializer

@api_view(['GET','POST'])
def create_room(request):
    query_set = request.data
    print('entered',query_set)
    user = User.objects.get(username = query_set['sender'])
    user1 = User.objects.get(username = query_set['reciever'])
    try:
        post = ChatRoom.objects.get(sender = user,reciever = user1)
    except:
        try:
            post = ChatRoom.objects.get(sender = user1,reciever = user)
        except:
            post = ChatRoom.objects.create(name = query_set['name'],sender = user,reciever = user1)
            post.save()
    
    serializer = ChatRoomSerializer(post)
    # if serializer.is_valid():
    #     serializer.save()
    return Response(serializer.data)
    

@api_view(['GET','POST']) 
def get_roomss(request):
    room = ChatRoom.objects.all()
    serializer = ChatRoomSerializer(room,many=True)
    return Response(serializer.data)  

@api_view(['GET','POST']) 
def view_message(request,id):
    msg = ChatMessage.objects.filter(room = id)
    print('msg',msg)
    serializer = ChatMessageSerializer(msg,many=True)
    if serializer:
        return Response(serializer.data)
    else:
        return Response('Nothing found')