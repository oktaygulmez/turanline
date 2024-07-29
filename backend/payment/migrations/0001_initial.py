# Generated by Django 5.0.2 on 2024-07-27 12:02

import django.db.models.deletion
import payment.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('expiration_date', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
                ('cardholder_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CardPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('comment', models.CharField(max_length=100)),
                ('content_type', models.ForeignKey(limit_choices_to=models.Q(('model', payment.models.Card)), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
