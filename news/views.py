import datetime as dt 
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
from .models import Article


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')


def convert_dates(dates):
    # Function that gets the weekely number of the date
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Sartuday','Sunday']

    # Returning the actual day of the week
    day = days[day_number]
    return day

def news_today(request):
    date = dt.date.today()
    news = Article.todays_news()
    return render(request, 'all_news/today_news.html',{"date": date,"news":news})
       
def past_days_news(request,past_date):
    try:
    # converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today)

    news = Article.days_news(date)
    return render (request, 'all_news/past_news.html',{"date": date, "news":news})

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all_news/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all_news/search.html',{"message":message})


def article(request,article_id):
    try:
        article= Article.objects.get(id = article_id)
    except:
        raise Http404()
    return render(request,"all_news/article.html", {"article":article})