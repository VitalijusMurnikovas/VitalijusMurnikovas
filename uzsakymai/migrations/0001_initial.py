# Generated by Django 4.0.3 on 2022-04-09 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UzsakymuListas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Pavadink šitą darbų seką kaip nors originaliai', max_length=100, verbose_name='Pavadinimas')),
            ],
            options={
                'verbose_name': 'Uzsakymu listas',
                'verbose_name_plural': 'Uzsakymu listai',
            },
        ),
        migrations.CreateModel(
            name='Uzsakymai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dalis', models.CharField(help_text='Reikalinga dalis', max_length=30, verbose_name='dalis')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uzsakymai.uzsakymulistas')),
            ],
            options={
                'verbose_name': 'Dalis',
                'verbose_name_plural': 'Dalys',
            },
        ),
    ]
