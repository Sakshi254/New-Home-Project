from django.shortcuts import render
from django.http import HttpResponse
from lists.choices import price_choices, bedroom_choices, state_choices
from lists.models import List

# Create your views here.
def index(request):
    list = List.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'Lists': list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request,'pages/index.html',context)
def about(request):
    return render(request,'pages/about.html')