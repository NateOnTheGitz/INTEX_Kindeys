# Generated by Django 4.1.2 on 2022-11-29 02:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=30)),
                ('sodium_mg', models.IntegerField(default=0)),
                ('protien_g', models.IntegerField(default=0)),
                ('water_L', models.IntegerField(default=0)),
                ('potassium_mg', models.IntegerField(default=0)),
                ('phos_mg', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'food_ingredient',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_desc', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'measurement',
            },
        ),
        migrations.CreateModel(
            name='Recommended_Levels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(default=0)),
                ('rec_sodium_mg', models.IntegerField(default=0)),
                ('rec_protien_g', models.IntegerField(default=0)),
                ('rec_water_L', models.IntegerField(default=0)),
                ('rec_potassium_mg', models.IntegerField(default=0)),
                ('rec_phos_mg', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'recommended_levels',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('stage', models.IntegerField(default=0)),
                ('comorbidity', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(default=0)),
                ('weight_lbs', models.IntegerField(default=0)),
                ('height_in', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'User Information',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='Food_Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('meal_type', models.CharField(max_length=50)),
                ('quantity', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('food_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trackerapp.food_ingredient')),
                ('measurement', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trackerapp.measurement')),
            ],
            options={
                'db_table': 'food_log',
            },
        ),
        migrations.AddField(
            model_name='food_ingredient',
            name='measurement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='trackerapp.measurement'),
        ),
    ]
