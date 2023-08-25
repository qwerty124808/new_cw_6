from django.shortcuts import render, get_object_or_404
from django.views.generic import (ListView, DetailView, TemplateView, 
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.forms import inlineformset_factory
from django.db import transaction
from django.http import Http404
from servise.models import Client, MailSettings
from servise.forms import ClientForm, MailSettingsForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "servise/home.html"



class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    def get_queryset(self, *args, **kwargs):
        queryset = Client.objects.filter(user=self.request.user)
        return queryset
        
class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("servise:Clients")

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super().form_valid(form)

class ClientUpdateViev(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("servise:Clients")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy("servise:Clients")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object


class MailSettingsListView(LoginRequiredMixin, ListView):
    model = MailSettings
    def get_queryset(self, *args, **kwargs):
        queryset = MailSettings.objects.filter(user=self.request.user)
        return queryset

class MailSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy("servise:Mails")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.filter(user=self.request.user)
        print(context)
        return context

    def form_valid(self, form):
        client = form.save(commit=False)
        client.user = self.request.user
        client.save()
        return super().form_valid(form)

class MailSettingsUpdateViev(LoginRequiredMixin, UpdateView):
    model = MailSettings
    form_class = MailSettingsForm
    success_url = reverse_lazy("servise:Mails")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object

class MailSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailSettings
    success_url = reverse_lazy("servise:Mails")

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.user != self.request.user:
            raise Http404
        return self.object
    