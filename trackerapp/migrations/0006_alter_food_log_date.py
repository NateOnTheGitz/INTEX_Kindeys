# Generated by Django 4.1.2 on 2022-11-30 03:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0005_rename_rec_water_l_by_kg_recommended_levels_rec_protein_g_by_kg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_log',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
