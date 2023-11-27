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

def ThingsDeteilView(request, id):
    if  request.method == "GET":
        show_id_key = get_object_or_404(Things, id=id)
        return  render(request, template_name='things/things_detail.html', context={"show_id_key":show_id_key})


def page1(request):
        return render(request,"things/page1.html", {'navbar':'page1'})
def page2(request):
        return render(request,"things/page2.html", {'navbar':'page2'})
def page3(request):
        return render(request,"things/page3.html", {'navbar':'page3'})
def page4(request):
        return render(request,"things/page4.html", {'navbar':'page4'})
