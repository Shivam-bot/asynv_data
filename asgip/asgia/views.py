from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
from django.http.response import HttpResponseRedirect
from .forms import *


def home(request):
    user_detail = UserDetail.objects.all()
    user_info = [{"id": data.id, 'first_name': data.first_name, 'last_name': data.last_name, 'email': data.email,
                  'mobno': data.mobno} for data in user_detail]
    context = {"user_info": user_info}

    return render(request, 'home.html',context)

@csrf_exempt
def userview(request):
    # try:
    user_dict = {}
    user_dict['user_data'] = userform()
    if request.method == "POST":
        user_data = user_dict['user_data'] = userform(request.POST or None)
        # print(user_data, "before")
        if user_data.is_valid():
            # print(user_data, "after")
            user_info = user_data.save()
            print(user_info)
            channel_layer = get_channel_layer()
            # notification_objs = UserDetail.objects.all().count()
            data = {'id':user_info.id,'first_name':user_info.first_name,'last_name':user_info.last_name,"email":user_info.email
                    ,"mob_no":user_info.mobno}
            async_to_sync(channel_layer.group_send)('test_consumer_group', {
                'type': 'send_notification',
                'value': json.dumps(data)
            })
            return HttpResponseRedirect('user')
        user_dict['error'] =user_data.errors
        print(user_data.errors)
        return render(request, 'user.html', user_dict)
    return render(request, 'user.html', user_dict)


