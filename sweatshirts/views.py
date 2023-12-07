from django.shortcuts import render, get_object_or_404
from . models import SweatShirts

from . import models
def SweatListView(request):
    shirts = models.SweatShirts.objects.all()
    context = {
        'shirts_key': shirts,

    }
    html_name = 'things/page2.html'
    return render(request, html_name, context)
def SweatDeteilView(request, id):
    if request.method == "GET":
        show_id_key = get_object_or_404(SweatShirts, id=id)
        return  render(request, template_name='things/things_detail.html', context={"show_id_key":show_id_key})

