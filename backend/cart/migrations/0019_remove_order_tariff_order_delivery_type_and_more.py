# Generated by Django 5.0.2 on 2024-07-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0018_remove_order_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='tariff',
        ),
        migrations.AddField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(blank=True, choices=[('HR', 'High-speed'), ('O', 'Optimal'), ('LC', 'Low-cost'), ('E', 'Express')], max_length=50, null=True, verbose_name='Тип доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='max_delivery_period',
            field=models.DateField(blank=True, null=True, verbose_name='Максимальный период доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='min_delivery_period',
            field=models.DateField(blank=True, null=True, verbose_name='Минимальный период доставки'),
        ),
    ]
