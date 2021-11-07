from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from FallInApp.models import User, Organization, OrgUser,Message, Response, ChatRoom
from FallInApp.serializers import UserSerializer,OrganizationSerializer,OrgUserSerializer,ChatRoomSerializer,MessageSerializer,ResponseSerializer



@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        users = User.objects.all()
        user_serializer=UserSerializer(users,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif request.method =='POST':
        user_data = JSONParser().parse(request) 
        user_serializer=UserSerializer(data=user_data) 
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("User added successfully",safe=False)
        return JsonResponse("Failed to add User")
    elif request.method=='PUT':
        user_data = JSONParser().parse(request) 
        user=User.objects.get(id=user_data['id'])
        user_serializer=UserSerializer(user,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated User successfully",safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        user=User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted successfully",safe=False)


