from django.shortcuts import render
from django.conf import settings
from newsapi import NewsApiClient

from .models import Headline, NewsItem

API_KEY = settings.NEWS_API_KEY
api = NewsApiClient(api_key=API_KEY)

def index(request, *args, **kwargs):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    headlines = Headline.objects.all()
    context = {'latest_headlines':headlines}
    return render(request, "news/headlines.html", context, status=200)

def get_headlines(request):
    '''
    #TODO: have this run daily to gather news
    ex. api.get_top_headlines()
    ex. api.get_everything(q='bitcoin')
        api.get_sources()

    '''
    headlines=api.get_top_headlines()
    l = headlines['articles']
    for article in l:
        headline = Headline.objects.create(
            source = article['source']['name'],
            author = article['author'],
            title = article['title'],
            description = article['description'],
            url = article['url'],
            urlToImage = article['urlToImage'],
            publishedAt = article['publishedAt'],
            content = article['content']
        )
        headline.save()
    desc,news,img=[],[],[]
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'news/news_index.html', context={"mylist":mylist})



def crypto_news(request):
    '''
    ex. api.get_top_headlines()
    ex. api.get_everything(q='bitcoin')
        api.get_sources()
    '''
    crypto_news=api.get_everything(q="crypto")
    l = crypto_news['articles']
    desc,news,img=[],[],[]
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news,desc,img)
    return render(request, 'news/news_index.html', context={"mylist":mylist})
