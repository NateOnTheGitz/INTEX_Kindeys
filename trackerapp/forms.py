# from django import forms
# from .models import 
from django import forms
from django.forms import ModelForm
from .models import Food_Log
from .models import Food_Ingredient
from .models import User


class DateInput(forms.DateInput):
    input_type = 'date'
class Food_Log_Form(forms.ModelForm):

  #  def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['date'].widget.attrs.update({'type': 'datetime-local'})
    class Meta:
        model = Food_Log
        fields = ['username', 'date', 'meal_type', 'food_name', 'quantity', 'measurement']
        widgets = {
            'date': DateInput()
        }


class Add_Food(forms.ModelForm) :
    class Meta:
        model = Food_Ingredient
        fields = '__all__'

class Create_User(forms.ModelForm) :
    class Meta:
        model = User
        fields=['first_name', 'last_name', 'email', 'gender', 'stage', 'comorbidity', 'date_of_birth', 'weight_lbs', 'height_in', 'username', 'password']
        widgets = {
            'date_of_birth': DateInput()
        }

