from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)  
    stage = models.IntegerField(default=0)
    comorbidity = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=0)
    weight_lbs = models.IntegerField(default=0)
    height_in = models.IntegerField(default=0)
    
    def __str__(self):
        return (self.full_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
        
    class Meta:
        verbose_name_plural = 'User Information'
        db_table = 'user'

class Measurement(models.Model):
    measurement_desc = models.CharField(max_length=20)

    def __str__(self):
        return (self.measurement_desc)
    
    class Meta:
        verbose_name_plural = 'Measurement'
        db_table = 'measurement'

class Food_Ingredient(models.Model):
    food_name = models.CharField(max_length=30)
    measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING)
    sodium_mg = models.IntegerField(default=0)
    protien_g = models.IntegerField(default=0)
    water_L = models.IntegerField(default=0)
    potassium_mg = models.IntegerField(default=0)
    phos_mg = models.IntegerField(default=0)  


    def __str__(self):
        return (self.food_name)
    
    class Meta:
        verbose_name_plural = 'Food Ingredient'
        db_table = 'food_ingredient'
    

class Recommended_Levels(models.Model):
    stage = models.IntegerField(default=0)
    rec_sodium_mg_min = models.IntegerField(default=0)
    rec_sodium_mg_max = models.IntegerField(default=0)
    rec_potassium_mg_min = models.IntegerField(default=0)
    rec_potassium_mg_max = models.IntegerField(default=0)
    rec_phos_mg_min = models.IntegerField(default=0)
    rec_phos_mg_max = models.IntegerField(default=0)
    rec_water_L_male = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    rec_water_L_female = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    rec_water_L_by_kg = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    
    def __str__(self):
        return (self.stage)
        
    class Meta:
        verbose_name_plural = 'Recommended Levels'

        db_table = 'recommended_levels'


class Food_Log(models.Model):
    date = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=0)
    meal_type = models.CharField(max_length=50)
    food_name = models.ForeignKey(Food_Ingredient, on_delete=models.DO_NOTHING)
    quantity = models.DecimalField(default=0, decimal_places=3, max_digits=10)
    measurement = models.ForeignKey(Measurement, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = 'Food Log'
        db_table = 'food_log'

    def __str__(self):
        return (self.date)

    