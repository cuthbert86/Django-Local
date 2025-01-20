from django.shortcuts import render
from newsapi import NewsApiClient

# Create your views here.
# newsapi = NewsApiClient(api_key='20fdaea9ef804a4096ca505c3eeeebb6')


def index(request):
    newsapi = NewsApiClient(api_key='20fdaea9ef804a4096ca505c3eeeebb6')
    top = newsapi.get_top_headlines(sources='techcrunch')
    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        mylist = zip(news, desc, img)

    return render(request, 'newsapp/index.html', context={"mylist": mylist})
