from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, TemplateView, 
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.forms import inlineformset_factory
from django.db import transaction
from servise.models import Client, MailSettings
from servise.forms import ClientForm, MailSettingsForm


class HomeView(TemplateView):
    template_name = "servise/home.html"



class ClientListView(ListView):
    model = Client
    def get_queryset(self, *args, **kwargs):
        queryset = Client.objects.filter(user=self.request.user)
        return queryset
        
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("servise:Clients")

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super().form_valid(form)

class ClientUpdateViev(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("servise:Clients")

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("servise:Clients")



class MailSettingsListView(ListView):
    model = MailSettings
    def get_queryset(self, *args, **kwargs):
        queryset = MailSettings.objects.filter(user=self.request.user)
        return queryset

class MailSettingsCreateView(CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy("servise:Mails")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(user=self.request.user)
        print(context)
        return context

    def form_valid(self, form):
        form.instance.client.set(Client.objects.filter(user=self.request.user))
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super().form_valid(form)

class MailSettingsUpdateViev(UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy("servise:Mails")

class MailSettingsDeleteView(DeleteView):
    model = MailSettings
    success_url = reverse_lazy("servise:Mails")
    