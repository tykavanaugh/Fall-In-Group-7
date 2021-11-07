from rest_framework import serializers
from FallInApp.models import User, Organization, OrgUser,Message, Response, ChatRoom

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','name','email','country','city','needs','urgency','details')


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Organization
        fields=('id','name','vetted','assistance_type','username','password')

class OrgUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrgUser
        fields=('id','name','password','email','org_id')

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=ChatRoom
        fields=('id','org_user_id','user_id','password')
    
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=('id','body','org_user_id','chatroom_id')

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Response
        fields=('id','body','user_id','message_id')
