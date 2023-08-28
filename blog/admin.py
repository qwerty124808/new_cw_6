from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Настройки админки для блога.
    """
    list_display = ('title', 'content', 'picture', 'create_date', 'is_published', 'views_count')


