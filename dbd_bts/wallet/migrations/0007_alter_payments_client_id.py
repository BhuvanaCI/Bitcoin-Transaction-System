# Generated by Django 3.2.9 on 2021-12-11 17:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_payments_cancelled'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='client_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
    ]
