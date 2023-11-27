from django.shortcuts import render
from . models import SweatShirts

from . import models
def ThingsListView(request):
    shirts = models.SweatShirts.objects.all()
    context = {
        'shirts_key': shirts,

    }
    html_name = 'sweatshirts/sweatshirts.html'
    return render(request, html_name, context)
