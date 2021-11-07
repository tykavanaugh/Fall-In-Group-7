# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'FallInChat/index.html')

#This will be updated to work with SQL system
def room(request, room_name):
    return render(request, 'FallInChat/room.html', {
        'room_name': room_name
    })