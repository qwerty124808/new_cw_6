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
        fields = ('title', 'body','time', 'mailing_periodicity', 'mailing_status', 'clients', 'get_clients_by_user')
        exclude=("clients",)
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

            'get_clients_by_user': forms.Select(attrs={
                'class': 'form-control',
            }),

        }
    # choices = []
    # get_clients_by_user = forms.ChoiceField(choices=choices)

    # def __init__(self, *args, **kwargs):
    #     # only change attributes if an instance is passed            
    #     instance = kwargs.get('instance')
    #     if instance:
    #         self.choices = instance.get_clients_by_user()
    #         kwargs["initial"] = {'get_clients_by_user': instance.get_clients_by_user()}
    #     super().__init__(*args, **kwargs)