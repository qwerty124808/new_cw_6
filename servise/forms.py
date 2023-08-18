from django import forms

from servise.models import Client, MailSettings

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'surname', 'email', 'comment')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя клиента',
                }),

            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия клиента',
                }),

            'surname': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Отчество клиента',
                }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Электронная почта клиента',
                }),

            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш комментарий',
                'rows': 2,
                }),
        }


class MailSettingsForm(forms.ModelForm):

    class Meta:
        model = MailSettings
        fields = ('title', 'body','time', 'mailing_periodicity', 'mailing_status', 'clients')
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема сообщения',
                }),
            
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст сообщения',
                'rows': 2,
                }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control',
            }),

            'mailing_periodicity': forms.Select(attrs={
                'class': 'form-control',
            }),
        }