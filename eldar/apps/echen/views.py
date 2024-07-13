from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from.models import Client
from django.views.generic import ListView, CreateView, DetailView, UpdateView


class ClientView(ListView):
    model = Client
    template_name = 'echen/index.html'
    context_object_name = 'client'


class CreateClient(CreateView):
      model = Client
      template_name = 'echen/create_client.html'
      fields = ['name', 'description', 'image']
      success_url = reverse_lazy('echen:Home')


class ViewClient(DetailView):
      model = Client
      template_name = 'echen/detail_client.html'


class UpdateClient(UpdateView):
    model = Client
    template_name = 'echen/update_client.html'
    fields = ['name', 'description', 'image']
    success_url = reverse_lazy('echen:Home')

