# Generated by Django 4.1.2 on 2022-11-29 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trackerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food_ingredient',
            options={'verbose_name_plural': 'Food Ingredient'},
        ),
        migrations.AlterModelOptions(
            name='food_log',
            options={'verbose_name_plural': 'Food Log'},
        ),
        migrations.AlterModelOptions(
            name='measurement',
            options={'verbose_name_plural': 'Measurement'},
        ),
        migrations.AlterModelOptions(
            name='recommended_levels',
            options={'verbose_name_plural': 'Recommended Levels'},
        ),
    ]