from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from .settings import BUS_STATION_CSV

def index(request):
    return redirect(reverse(bus_stations))


def read_csv_file(csvfile):
    context = list()
    with open(csvfile, "r") as f_obj:
        reader = csv.reader(f_obj)
        next(reader)
        for row in reader:
            context.append({'Name': row[1], 'Street': row[4], 'District': row[6]})

    return context


def bus_stations(request):

    content = read_csv_file(BUS_STATION_CSV)

    current_page = int(request.GET.get('page', 1))
    elements_per_page = 10

    paginator = Paginator(content, elements_per_page)
    page = paginator.get_page(current_page)
    page_content = page.object_list

    max = paginator.num_pages
    if current_page > max:
        current_page = max

    if page.has_previous():
        prev_page_url = f'{reverse(bus_stations)}?page={page.previous_page_number()}'
    else:
        prev_page_url = None

    if page.has_next():
        next_page_url = f'{reverse(bus_stations)}?page={page.next_page_number()}'
    else:
        next_page_url = None

    return render(request, 'index.html', context={
        'bus_stations': page_content,
        'current_page': current_page,
        'prev_page_url': prev_page_url,
        'next_page_url': next_page_url,
    })

