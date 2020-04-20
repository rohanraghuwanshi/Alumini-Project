from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json


@login_required
def chats(request):
    return render(request, 'chatapp/room.html', {})

@login_required
def chatroom(request, room_name):

    context = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'username': mark_safe(json.dumps(request.user.username)),
    }

    return render(request, 'chatapp/room.html', context)
