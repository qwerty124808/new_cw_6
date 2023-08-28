from django.db import models
from datetime import date

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    picture = models.ImageField(upload_to='', **NULLABLE)
    create_date = models.DateField(default=date.today(), verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=False, verbose_name='состояние')
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'