from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_home(request):
    context = {'name': 'پوریا دادخواه'}
    return render(request, 'website/index.html', context)
