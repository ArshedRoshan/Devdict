from rest_framework import serializers
from.models import User,follow,profile,Application
from post . serializers import postSerializers,saveSerializer


class followSerialiazers(serializers.ModelSerializer):

    class Meta:
        model = follow
        fields = ['id','follower','following']     
        
    
    
class profileSerializers(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ['id','user','profile_picture','bio']

class applicationSerializers(serializers.ModelSerializer):
    applicants = serializers.SerializerMethodField('get_user')
    companyName = serializers.SerializerMethodField('get_company')
    class Meta:
        model = Application
        fields = ['id','user','Full_Name','Qualification','Phone_number','resume','company_name','applicants','processing','Accept','Decline','companyName']
        
    def get_user(self,user):
        return user.user.get_username() 
    
    def get_company(self,user):
        return user.company_name.company_name





class UserSerializers(serializers.ModelSerializer):
    users = postSerializers(many=True)
    pro = profileSerializers(many=True)
    following = followSerialiazers(many=True)
    followers = followSerialiazers(many=True)
    jobs = applicationSerializers(many=True)
    com = applicationSerializers(many=True)
    saved_user = saveSerializer(many = True)
    
    
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email','password','username','phone_number','Account_type','users','company_name','Describe_company','hiring_for','pro','following','followers','follow','follower','jobs','com','saved_user','is_active','is_block','is_admin']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance 

# class followSerialiazers(serializers.ModelSerializer):
#     class Meta:
#         model = follow
#         fields = ['id','follower','following']

class follow1Serialiazers(serializers.ModelSerializer):
    class Meta:
        model = follow
        fields = ['id','follower','following']
        
        depth = 1

        
# class UsersaveSerializers(serializers.ModelSerializer):
#     saved_user = saveSerializer(many = True)
#     class Meta:
#         model = User
#         fields = ['id','first_name','last_name','email','password','username','phone_number','Account_type','company_name','Describe_company','hiring_for','saved_user']
