from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
import time

def menu(request, item):
    #checking in cache
    cached_item = cache.get(item)
    if cached_item:
        print("found in cache"*7 )
        return JsonResponse({"message":"Item from menu fetched successfuly", "data": cached_item, "source": "cache"})
    
    #checking db
    # print("not found in cache"*7, cache.get('jollofrice') )

    time.sleep(5)
    order = f"{item} with fries and two juice" #change later to show staleness 
    #store in cache, since cache has missed it
    
    cache.set(item, order, timeout=120)
    return JsonResponse({"item": order, "source": "database"})
