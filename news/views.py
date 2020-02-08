from django.shortcuts import render
from django.conf import settings
from newsapi import NewsApiClient

API_KEY = settings.NEWS_API_KEY
api = NewsApiClient(api_key=API_KEY)

def tech_news(request):
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
