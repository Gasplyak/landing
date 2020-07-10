from django.urls import path

from .views import *

urlpatterns = [
    path('', redirect_on_main, name='redirect_on_main_url'),
    path('home/', main_page, name='main_page_url'),
    path('main/', redirect_on_main, name='redirect_on_main_url'),
    path('range/', range_page, name='range_page_url'),
    path('detail/<str:slug>/', detail_page, name='detail_page_url'),
    path('distribs/', distribs_page, name='distribs_page_url'),
    path('help/', help_page, name='help_page_url'),
    path('basket/', basket_page, name='basket_page_url'),
    path('add/', add_to_basket, name='adding'),
    path('remove/', remove_from_basket, name='removing')
]
