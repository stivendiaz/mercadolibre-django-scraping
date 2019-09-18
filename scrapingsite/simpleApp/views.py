from django.shortcuts import render
from django.http import JsonResponse

import src.scrapers.mercadolibre as mercadolibre

from .models import Product


def index(request):
     return render(request, 'simpleApp/index.html')

def search(request, search):
     total_results = int(request.GET.get('total'))

     result = mercadolibre.callScrap(search)

     for data in result:
        product = Product(title=data.get('title'), price=data.get('price'))
        product.save()

     return JsonResponse({
          'search': search,
          'total_results': total_results,
          'products': result[:total_results],
     })
