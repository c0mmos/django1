from django.urls import path, include
from base_site.views import *

app_name = 'website'

urlpatterns = [
    path('', index_home, name='index'),
]
