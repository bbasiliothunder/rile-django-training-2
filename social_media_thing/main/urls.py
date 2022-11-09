from typing import List
from django.urls import path
from main.views import index

urlpatterns: List[path] = [
    path('', index, name='index')
]