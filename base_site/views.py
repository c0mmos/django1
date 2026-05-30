from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_home(request):
    return render(request, 'website/index.html')
