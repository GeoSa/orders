# Generated by Django 3.0.1 on 2020-10-01 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_number', models.CharField(blank=True, max_length=20)),
                ('customer_address', models.CharField(blank=True, max_length=150)),
                ('customer', models.CharField(blank=True, max_length=150)),
                ('order_type', models.SmallIntegerField(default=2)),
                ('valid', models.BooleanField(default=True)),
                ('paid_time', models.DateTimeField(null=True)),
                ('paid_status', models.SmallIntegerField(default=2)),
                ('order_amount', models.IntegerField(null=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('moderation_time', models.DateTimeField(null=True)),
                ('approve_status', models.SmallIntegerField(default=2)),
                ('approve_time', models.DateTimeField(null=True)),
                ('rp_approve_time', models.DateTimeField(null=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('repeat_moderation_time', models.DateTimeField(null=True)),
                ('repeat_approve_time', models.DateTimeField(null=True)),
                ('order_source', models.SmallIntegerField(blank=True, default=2)),
                ('paid_order_amount', models.IntegerField(null=True)),
                ('status', models.SmallIntegerField(default=1, verbose_name='Order status')),
                ('archive', models.BooleanField(default=False)),
                ('payments', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewScans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scans', models.ImageField(upload_to='review/scans')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scans', to='order.Review')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='review/images')),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='order.Review')),
            ],
        ),
    ]
