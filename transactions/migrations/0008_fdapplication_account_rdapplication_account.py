# Generated by Django 4.2.14 on 2024-08-04 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_profile'),
        ('transactions', '0007_rdapplication_fdapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='fdapplication',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userbankaccount'),
        ),
        migrations.AddField(
            model_name='rdapplication',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userbankaccount'),
        ),
    ]