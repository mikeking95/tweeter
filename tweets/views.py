from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Tweet

def home_view(request, *args, **kwargs):
    print(f"Args:{args} | Kwargs: {kwargs}")
    return HttpResponse("<h1>Hi Mom!</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    try:
        obj=Tweet.objects.get(id=tweet_id)
    except:
        raise Http404
    return HttpResponse(f"<h1>Hi {tweet_id}!</h1><p>{obj.content}")