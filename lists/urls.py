from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ListViewSet

router = routers.DefaultRouter()
router.register(r'',ListViewSet,basename="post")

urlpatterns = [
    path('',views.lists, name='lists'),
    path('<int:list_id>',views.list, name='list'),
    path('search',views.search, name='search'),
    path('api/',include(router.urls)),
    path('list-api/',views.ApiView.as_view(), name = 'Output'),
  ##  path('post',views.addData, name = 'Input'),
]
