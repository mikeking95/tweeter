from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [ {"id": x.id, "content": x.content} for x in qs ]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def home_view(request, *args, **kwargs):
    print(f"Args:{args} | Kwargs: {kwargs}")
    return render(request, 'pages/home.html', context={}, status=200)

def about_view(request, *args, **kwargs):
    print(f"Args:{args} | Kwargs: {kwargs}")
    return render(request, 'pages/about.html', context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        obj=Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found!'
        status = 404
    return JsonResponse(data, status=status)
