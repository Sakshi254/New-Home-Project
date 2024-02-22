from django.shortcuts import get_object_or_404, render
from django.core import serializers
from .models import List
from django.http import HttpResponse, HttpRequest
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .choices import price_choices, bedroom_choices, state_choices
from rest_framework.response import Response
from rest_framework.views import APIView
from lists.serializers import ListSerializer, ListFilters
from rest_framework import status, viewsets, filters, generics
import django_filters.rest_framework
# Create your views here.

def lists(request):
    Lists = List.objects.order_by('-list_date')
    paginator = Paginator(Lists,3)
    page = request.GET.get('page')
    paged_Lists = paginator.get_page(page)
    context= {
        'Lists' : paged_Lists
    }
    return render(request,'lists/lists.html',context)

def list(request, list_id):
    list = get_object_or_404(List, pk=list_id)
    context = { 
        'list':list
    }
    return render(request,'lists/list.html',context)

def search(request):
    queryset_list = List.objects.order_by('-list_date')
 
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
          queryset_list = queryset_list.filter(description__icontains = keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
          queryset_list = queryset_list.filter(city__iexact = city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
          queryset_list = queryset_list.filter(state__iexact = state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
          queryset_list = queryset_list.filter(bedrooms__iexact = bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
          queryset_list = queryset_list.filter(price__lte= price)
    
    context = {
        'Lists': queryset_list,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request,'lists/search.html',context)

class ApiView(APIView):
   """API View"""

   ## serializer_class = serializers.ListSerializer

   def get(self, request, format=None):
      data = List.objects.all()
      serializer = ListSerializer(data, many =True)
      return Response(serializer.data)
   
   def post(self,request):
      serializer = ListSerializer(data = request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data,status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
   
   def search(self,request):
      pass
      
   
class ListViewSet(viewsets.ModelViewSet):
   queryset = List.objects.all()
   serializer_class = ListSerializer
   #search_fields =['city','state','bedrooms','bathrooms','price','garage']
   #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
   filterset_class = ListFilters
   
