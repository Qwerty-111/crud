from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .forms import *
from .models import *


class Read(ListView):
    model = Person
    template_name = 'crud_app/read.html'
    context_object_name = 'person'


def create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            Person.objects.create(**form.cleaned_data)
            redirect('read')
    else:
        form = PersonForm()
    return render(request, 'crud_app/create.html', {'form': form})


class Update(ListView):
    model = Person
    template_name = 'crud_app/update.html'
    context_object_name = 'person'


def update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
            return redirect('read')
    else:
        form = PersonForm(instance=person)
    return render(request, 'crud_app/update.html', {'form': form})


def delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return redirect('read')
