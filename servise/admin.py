from django.contrib import admin
from servise.models import Client, MailSettings
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    """
    Настройки админки для клиента.
    """
    list_display = ('email', 'first_name', 'last_name', 'surname', 'comment')


@admin.register(MailSettings)
class MailSettingsAdmin(admin.ModelAdmin):
    """
    Настройки админки для рассылки.
    """
    list_display = ('title', 'body', 'time', 'mailing_periodicity', 'mailing_status', 'mailing_is_active')