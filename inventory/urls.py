from django.urls import path
from .views import item_detail

from django.urls import path
from .views import item_list, item_detail

urlpatterns = [
    path('items/', item_list, name='item_list'),
    path('items/<int:item_id>/', item_detail, name='item_detail'),
]

