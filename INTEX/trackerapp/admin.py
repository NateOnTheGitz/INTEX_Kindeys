from django.contrib import admin

# Register your models here.
from .models import User
from .models import Measurement
from .models import Food_Ingredient
from .models import Recommended_Levels
from .models import Food_Log

admin.site.register(User)
admin.site.register(Measurement)
admin.site.register(Food_Ingredient)
admin.site.register(Recommended_Levels)
admin.site.register(Food_Log)
