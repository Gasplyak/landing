from django.shortcuts import render, redirect
from .models import *

from django.db.models import Q


def main_page(request):
    return render(request, 'land/main.html')

def range_page(request):
    search_query = request.GET.get('search', '')

    if search_query:
        goods = Good.objects.filter(Q(title__icontains=search_query) | Q(content__icontains=search_query))
    else:
        goods = Good.objects.all()

    return render(request, 'land/range.html', context={'goods': goods})


def detail_page(request, slug):
    good = Good.objects.get(slug__iexact=slug)
    return render(request, 'land/good_detail.html', context={'good': good})

def distribs_page(request):
    return render(request, 'land/distribs.html')

def help_page(request):
    return render(request, 'land/help.html')

def redirect_on_main(request):
    return redirect('main_page_url')

def basket_page(request, slug):
    good = Good.objects.get(slug__iexact=slug)
    return render(request, 'land/basket.html', context={'goods': good})

def add_to_basket(request, slug):
    pass

def remove_from_basket(request, slug):
    pass