# Generated by Django 4.2.3 on 2023-08-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servise', '0003_alter_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsettings',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='состояние'),
        ),
    ]