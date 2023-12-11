from django.contrib.auth import logout
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView
from .forms import ThingForm
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

def thing_update(request, id):
    thing = get_object_or_404(Things, id=id)

    if request.method == 'POST':
        form = ThingForm(request.POST, instance=thing)
        if form.is_valid():
            form.save()
            return redirect('page2')
    else:
        form = ThingForm(instance=thing)

    return render(request, 'things/things_form.html', {'form': form, 'thing': thing})


def thing_delete(request, id):
    thing = get_object_or_404(Things, id=id)
    if request.method == 'POST':
        thing.delete()
        return redirect('page2')
    # Optionally, render a confirmation template for GET requests.
    return render(request, 'things/things_confirm_delete.html', {'thing': thing})

def create_thing(request):
    if request.method == 'POST':
        form = ThingForm(request.POST, request.FILES)
        if form.is_valid():
            new_thing = form.save(commit=False)
            new_thing.user = request.user
            new_thing.save()
            return redirect('things_list')
    else:
        form = ThingForm()

    return render(request, 'things/create_thing.html', {'form': form})



def things_list_view(request):
    things = Things.objects.all()
    return render(request, 'things/things_list.html', {'things': things})

def logout_view(request):
    logout(request)
    # Дополнительные действия после выхода из аккаунта, если необходимо
    return redirect('some_view')
