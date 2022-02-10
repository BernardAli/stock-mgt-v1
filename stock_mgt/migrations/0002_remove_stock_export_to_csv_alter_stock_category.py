# Generated by Django 4.0.2 on 2022-02-10 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_mgt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='export_to_CSV',
        ),
        migrations.AlterField(
            model_name='stock',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stock_mgt.category'),
        ),
    ]