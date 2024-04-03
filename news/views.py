import requests
import xmltodict

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from bs4 import BeautifulSoup as BSoup

from news.models import Headline


def scrape(request):

    # url = "https://english.onlinekhabar.com/feed/"
    # url = "https://newspolar.com/feed/"
    # url = "https://www.prasashan.com/feed/"
    urls = [
        "https://english.onlinekhabar.com/feed/",
        "https://newspolar.com/feed/",
        "https://www.prasashan.com/feed/",
    ]
    

    for u in urls:

        response = requests.get(u)
        content = response.content
        data_dict = xmltodict.parse(content)

        for data in data_dict:
            news_items = data_dict.get("rss").get("channel").get("item")
            for news in news_items:
                title = news["title"]
                desc = news["description"]
                url = news["link"]
                news_obj = Headline.objects.filter(title=title)
                if news_obj.exists()==False:
                    Headline.objects.create(title=title, description=desc, url=url)
                else:
                    pass
                # return HttpResponse(desc)
                print(news)

    return redirect("../")


def news_list(request):
    headlines = Headline.objects.all().order_by('-id')
    context = {
        "object_list": headlines,
    }
    return render(request, "news/home.html", context)
