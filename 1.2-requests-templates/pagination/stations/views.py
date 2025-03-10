from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from django.core.paginator import Paginator

def stations():
    list_stations = []
    with open('pagination/data-398-2018-08-30.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            list_stations.append(row)
    return list_stations

database = stations()

def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_number = request.GET.get('page', 1)
    paginator = Paginator(database, 10)
    page = paginator.get_page(page_number)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
