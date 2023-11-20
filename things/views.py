from django.shortcuts import render, get_list_or_404

from . import models
def ThingsListView(request):
    show = models.Things.objects.all()
    context = {
        'show_key': show,

    }
    html_name = 'things/things.html'
    return render(request, html_name, context)

def ThingsDeteilView(request, id):
    show_id = get_list_or_404(models.Things, id=id)
    context = {
        'show_id_key': show_id,
    }

    html_detaill_name = 'things/things.html'
    return render(request, html_detaill_name, context)
