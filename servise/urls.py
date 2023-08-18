from django.urls import path
from servise.views import (HomeView, 
                           ClientCreateView, ClientListView, ClientUpdateViev, ClientDeleteView,
                            MailSettingsListView, MailSettingsCreateView, MailSettingsUpdateViev, MailSettingsDeleteView
)
from servise.jobs import test_job
from servise.forms import MailSettingsForm
from servise.apps import ServiseConfig
app_name = ServiseConfig.name

urlpatterns = [
    path('aaa/', test_job),
    path('', HomeView.as_view(), name='home'),
    path('/clients/', ClientListView.as_view(), name='Clients'),
    path('/clientcreate/', ClientCreateView.as_view(), name='Clientcreate'),
    path('/clientupdate/<int:pk>/', ClientUpdateViev.as_view(), name='Clientupdate'),
    path('/clientdelete/<int:pk>/', ClientDeleteView.as_view(), name='Clientdelete'),

    path('/mails/', MailSettingsListView.as_view(), name='Mails'), 
    path('/mailcreate/', MailSettingsCreateView.as_view(), name='Mailcreate'),
    path('/mailupdate/<int:pk>/', MailSettingsUpdateViev.as_view(), name='Mailupdate'),
    path('/maildelete/<int:pk>/', MailSettingsDeleteView.as_view(), name='Maildelete'),
]