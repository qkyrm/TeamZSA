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
    # show_id = get_list_or_404(Things, id=id)
    # show = models.Things.objects.all()
    # context = {
    #     'show_id_key': show_id,
    # }
    # html_detail_name = 'things/things_detail.html'
    # return render(request, html_detail_name, context)
    if  request.method == "GET":
        show_id_key = get_object_or_404(Things, id=id)
        return  render(request, template_name='things/things_detail.html', context={"show_id_key":show_id_key})
