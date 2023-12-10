from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from .models import Things
from . import models


def ThingsListView(request):
    show = models.Things.objects.all()
    context = {
        'show_key': show,

    }
    html_name = 'things/things.html'
    return render(request, html_name, context)

def ThingsDetailView(request, id):
    if  request.method == "GET":
        show_id_key = get_object_or_404(Things, id=id)
        return render(request, template_name='things/things_detail.html', context={"show_id_key":show_id_key})

def page1(request):
        return render(request,"things/page1.html", {'navbar':'page1'})
def SweatListView(request):
        shirts = models.Things.objects.filter(type='shirt')

        context = {'shirts': shirts}
        html_name = 'things/page2.html'
        return render(request, html_name, context)
def MugListView(request):
        mugs = models.Things.objects.filter(type='mug')

        context = {'mugs': mugs}
        html_name = 'things/page3.html'
        return render(request, html_name, context)

def BagListView(request):
        bags = models.Things.objects.filter(type='bag')

        context = {'bags': bags}
        html_name = 'things/page4.html'
        return render(request, html_name, context)

def TshirtListView(request):
        tshirts = models.Things.objects.filter(type='tshirt')

        context = {'tshirts': tshirts}
        html_name = 'things/page5.html'
        return render(request, html_name, context)

