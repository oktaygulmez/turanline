# Generated by Django 5.0.2 on 2024-07-28 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_order_total_sum'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='tariff',
            field=models.JSONField(blank=True, null=True, verbose_name='Выбранный тариф доставки'),
        ),
    ]
