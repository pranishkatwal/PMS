# Generated by Django 3.2 on 2021-04-21 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_medicinetransaction_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinetransaction',
            name='is_final_entry',
            field=models.BooleanField(default=False),
        ),
    ]
