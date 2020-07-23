from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from rest_framework import serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

from fb_post.utils import get_post

from django.utils.dateparse import parse_datetime

import pytz

# @api_view(['GET','POST'])
def set_timezone(request, post_id):
    post_details = get_post(post_id)
    
    naive = parse_datetime(post_details['posted_at'])
    print(naive)
    user_tz=pytz.timezone('Europe/Helsinki')
    user_timzone=user_tz.normalize(
        naive.astimezone(user_tz)
        )
    user_updated_datetime = user_timzone.strftime('%Y-%m-%d %H:%M:%S.%f')
    post_details['posted_at'] = user_updated_datetime
    print(post_details)
    return HttpResponse(post_details)