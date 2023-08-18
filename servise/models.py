from django.db import models
from users.models import NULLABLE, User
from django.db.models import TextChoices
from config.settings import AUTH_USER_MODEL



class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    surname = models.CharField(max_length=150, verbose_name='отчество')
    comment = models.TextField(verbose_name='коментарий', **NULLABLE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self) -> str:
    #     return f'{self.last_name} {self.first_name} {self.surname}, email: {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = "клиенты"
        ordering = ('first_name', 'last_name', 'surname')


class MailSettings(models.Model):

    periodicity = [
        ('d', 'day'),
        ('w', 'week'),
        ('m', 'month')
    ]
    status = [
        ('c', 'create'),
        ('s', 'start'),
        ('f', 'finish')
    ]
    
    title = models.CharField(max_length=150, verbose_name='тема письма', **NULLABLE)
    body = models.TextField(verbose_name='письмо')
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='время  начала рассылки')
    mailing_periodicity = models.CharField(max_length=40, verbose_name='периодичность', choices=periodicity)
    mailing_status = models.CharField(max_length=20, verbose_name='cтатус', default='c', choices=status)
    mailing_is_active = models.BooleanField(default=True, verbose_name='Рассылка активна')
    clients = models.ManyToManyField(Client, verbose_name='клиенты')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

    # def __str__(self) -> str:
    #     return f'Тема: {self.title} \
    #             Текст: {self.body},\
    #             Время: {self.time}, \
    #             Периодичность: {self.mailing_periodicity}, \
    #             Статус: {self.mailing_status}'

    class Meta:
        verbose_name = 'Настройки рассылки'
        verbose_name_plural = "Настройки рассылок"
        ordering = ('mailing_status', )


class Log(models.Model):
    last_try_date = models.DateTimeField(auto_now_add=True, verbose_name='дата и время попытки')
    try_status = models.CharField(max_length=250, verbose_name='статус попытки')
    server_response = models.CharField(max_length=250, verbose_name='ответ сервера', **NULLABLE)
    user = models.ForeignKey(Client, verbose_name='пользователь', on_delete=models.CASCADE)
    mail = models.ForeignKey(MailSettings, on_delete=models.CASCADE, verbose_name='рассылка')

    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'
        ordering = ('last_try_date', )

    def __str__(self) -> str:
        return f'Дата попытки: {self.last_try_date},' + \
               f'Статус: {self.try_status},' + \
               f'Ответ сервера: {self.server_response}'
