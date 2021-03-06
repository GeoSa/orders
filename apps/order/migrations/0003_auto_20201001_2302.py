# Generated by Django 3.0.1 on 2020-10-01 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('order', '0002_auto_20201001_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='region.City'),
        ),
        migrations.AlterField(
            model_name='order',
            name='region',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='region.Region'),
        ),
    ]
