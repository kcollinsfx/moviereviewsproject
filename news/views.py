from django.shortcuts import render
from .models import News

def news(request):
    # order_by('-date') orders the news posts by descending order
    newss = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss':newss})