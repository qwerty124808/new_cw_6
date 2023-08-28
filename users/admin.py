from django.contrib import admin
from users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Настройки админки для пользователя.
    """
    list_display = ('email', 'fio', 'is_active')
