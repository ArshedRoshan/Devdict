from rest_framework import serializers
from . models import post,Like,question,comment,question_like,answers,answer_like,comment_reply,save_question


class comment_replySerializers(serializers.ModelSerializer):
    class Meta:
        model = comment_reply
        fields = ('id','Comment','commented_by','content')
        
class commentSerializers(serializers.ModelSerializer):
    comms = comment_replySerializers(many = True)
    class Meta:
        model = comment
        fields=('id','commented_by','content','Post','comms')
        
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= Like
        fields=('id', 'Post', 'likeusers')
        
    def get_likeusers_count(self, obj):
        return obj.likeusers.count()
        
class postSerializers(serializers.ModelSerializer):
    posts = commentSerializers(many=True)
    post_likes = LikeSerializer(many = True)
    class Meta:
        model = post
        fields=['id','caption','image','user','likes_count','posts','post_likes','is_active']
        
    def create(self, validated_data):
       return post.objects.create(**validated_data)
   
   

class quelikeSerializers(serializers.ModelSerializer):
    user_liked = serializers.SerializerMethodField()
    class Meta:
        model = question_like
        fields = ('id','Question','likeusers','userliked')
        
class answerlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = answer_like
        fields = ('id','Answer','liked_by')

class answerSerializers(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField('get_user')
    class Meta:
        model = answers
        fields = ('id','user','Question','answer','userinfo','like')

    def get_user(self,user):
        return user.user.get_username()
    
class saveSerializer(serializers.ModelSerializer):
    class Meta:
        model = save_question
        fields = ('id','user','saved_question')
        
    

class questionSerializers(serializers.ModelSerializer):
    userinfo = serializers.SerializerMethodField('get_user')
    questionss = answerSerializers(many=True)
    class Meta:
        model = question
        fields=('id','user','title','body1','userinfo','like','body2','questionss')

    def get_user(self,user):
        return user.user.get_username()
       
class questionSaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = question
        fields=('id','user','title','body1','like','body2')
   