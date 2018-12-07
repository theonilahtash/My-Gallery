from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Article


# Create your views here.
# def welcome(request):
#     return render(request,'welcome.html')
def gallery(request):
    return render (request,'welcome.html')

def photos(request):
    date = dt.date.today()
    photos = Article.todays_photos()
    return render(request, 'all-photos/today-photos.html', {"date": date,"photos":photos})

    convert_dates(dates)
    # Function that gets weekday number for the dates.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Sarturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_photos(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()

    if date == dt.date.today():
        return redirect(photos_of_day)

    return render(request,'all-photos/past-photos.html',{"date":date})

      
