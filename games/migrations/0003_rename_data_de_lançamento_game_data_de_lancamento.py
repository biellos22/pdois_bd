# Generated by Django 5.0.6 on 2024-06-24 20:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_rename_release_date_game_data_de_lançamento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='data_de_lançamento',
            new_name='data_de_lancamento',
        ),
    ]
