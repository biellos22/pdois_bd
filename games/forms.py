# games/forms.py

from django import forms
from .models import Game
import datetime

class GameForm(forms.ModelForm):
    data_de_lancamento = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'dd-mm-yyyy'}),
        label='Data de Lançamento',
        help_text='Formato: dd-mm-yyyy'
    )
    
    class Meta:
        model = Game
        fields = ['nome', 'empresa', 'data_de_lancamento']

    def clean_data_de_lancamento(self):
        data_de_lancamento = self.cleaned_data['data_de_lancamento']
        if isinstance(data_de_lancamento, datetime.date):
            return data_de_lancamento
        
        try:
            data_formatada = datetime.datetime.strptime(data_de_lancamento, '%d-%m-%Y')
            return data_formatada.date()
        except ValueError:
            raise forms.ValidationError('Formato de data inválido. Use o formato dd-mm-yyyy.')
