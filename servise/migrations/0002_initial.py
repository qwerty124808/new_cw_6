# Generated by Django 4.2.3 on 2023-08-17 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsettings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='log',
            name='mail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servise.mailsettings', verbose_name='рассылка'),
        ),
        migrations.AddField(
            model_name='log',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='servise.client', verbose_name='пользователь'),
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
