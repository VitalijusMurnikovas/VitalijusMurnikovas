# Generated by Django 4.0.3 on 2022-03-20 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registracija', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='darbulistas',
            options={'verbose_name': 'Darbu listas', 'verbose_name_plural': 'Darbų listai'},
        ),
        migrations.AlterField(
            model_name='darbulistas',
            name='title',
            field=models.CharField(help_text='Pavadink šitą darbą kaip nors originaliai', max_length=100, verbose_name='Pavadinimas'),
        ),
    ]
