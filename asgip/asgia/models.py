from django.db import models
from django.contrib.auth.models import User
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

class Notification(models.Model):

    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.TextField()
    is_seen = models.BooleanField(default=False)

    class Meta:
        db_table = "Notification"

    def save(self, *args, **kwargs):
        channel_layer = get_channel_layer()
        notification_objs = Notification.objects.filter(is_seen = False).count()
        data = {'count':notification_objs, 'current_notification':self.notification}
        async_to_sync(channel_layer.group_send)('test_consumer_group', {
            'type':'send_notification',
            'value':json.dumps(data)
        }) 
        super(Notification, self).save(*args, **kwargs)


class UserDetail(models.Model):

    objects = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobno = models.TextField()

    class Meta:
        db_table = "user_info"

