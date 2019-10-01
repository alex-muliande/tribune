import datetime as dt 
from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect


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

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all_news/today_news.html', {"date":date,}) 
    
       
def past_days_news(request,past_date):
    try:
    # converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error ValueError is thrown
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all_news/past_news.html', {"date":date})