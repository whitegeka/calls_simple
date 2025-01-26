from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [
    path('', CallsIndex.as_view()),
    path('get/calls', GetLastCalls.as_view(), name='get_calls'),
]
