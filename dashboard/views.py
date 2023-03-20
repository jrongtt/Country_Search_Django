from django.shortcuts import render
from .models import Data
from django.db.models import Q

# Create your views here.


def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
        # multiple_q = Q(Q(country_name__icontains=q) | Q(country_name__icontains=q))
        # print(multiple_q)
        # print(country_name__icontains=q)
        # print(q)
        data = Data.objects.filter(country_name__icontains=q)
        #data = multiple_q
    else:
        data = Data.objects.all()
        #data = ''
    context = {
        'data': data
    }
    return render(request, 'dashboard/index.html', context)