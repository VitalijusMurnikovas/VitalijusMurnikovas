# Generated by Django 4.0.3 on 2022-04-09 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uzsakymai', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzsakymai',
            name='list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uzsakymai.uzsakymulistas'),
        ),
    ]
