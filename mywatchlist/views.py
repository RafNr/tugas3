from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_watchlist = MyWatchList.objects.all()
    context = {
        'list_watch': data_watchlist,
    }

    return render(request, "watchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")