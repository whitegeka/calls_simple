from datetime import datetime, timedelta, timezone

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Calls


class SelfMixin(object):
    """
    The class work in datestart
    """
    def get_datestart(self):
        return datetime.now(timezone.utc)-timedelta(days=2)


class CallsIndex(ListView, SelfMixin):
    models = Calls
    template_name = 'calls/index.html'
    context_object_name = 'list_calls'

    def get_queryset(self):
        return Calls.objects.filter(
                date_of_call__gte=self.get_datestart()
            ).order_by('-id')

    def get_context_data(self, *args, **kwargs):
        context = super(CallsIndex, self).get_context_data(**kwargs)
        try:
            context['last_element'] = context['object_list'][0].pk
        except:
            context['last_element'] = 0
        return context


class GetLastCalls(View, SelfMixin):
    """
    The class returns a new call 
    
    return: json data
    """
    def get(self, request, *args, **kwargs):
        data = {'last_element': request.GET.get('last_element')}
        list_calls = Calls.objects.filter(
                date_of_call__gte=self.get_datestart()
            )
        sort_calls = list_calls.filter(pk__gt=str(int(data['last_element'])))
        if len(sort_calls) == 0:
            return JsonResponse(data)
        else:
            obj = sort_calls[0]
        data['string'] = render_to_string('calls/row_calls.html', {
            'call': obj,
            }, request=request)
        data['last_element'] = obj.pk
        return JsonResponse(data)
