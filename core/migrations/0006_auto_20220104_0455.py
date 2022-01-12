# Generated by Django 3.2.9 on 2022-01-04 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_client_mesure_mesure_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mesure',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='mesure',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.mesure'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='mesure',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.mesure'),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='phone',
            field=models.CharField(blank=True, max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='whatsapp_phone',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
    ]
