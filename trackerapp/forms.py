# from django import forms
# from .models import 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Food_Log
from .models import Food_Ingredient
from .models import Person
from crispy_forms.layout import Hidden
from django.forms import ModelForm, HiddenInput, ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'
class Food_Log_Form(forms.ModelForm):

  #  def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['date'].widget.attrs.update({'type': 'datetime-local'})
    class Meta:
        model = Food_Log
        fields = '__all__'
        exclude = ['username']
        widgets = {
            'date': DateInput()
        }


class Add_Food(forms.ModelForm) :
    class Meta:
        model = Food_Ingredient
        fields = '__all__'

class Person_info(forms.ModelForm) :
    userdata = User.objects.all()
    # curr_username = User.username 
    # Hidden('username', curr_username)
    # def __init__(self, *args, **kwargs):
    #     super(Person_info, self).__init__(*args, **kwargs)
        # self.fields['username'].widget = HiddenInput()
        # self.fields['password'].widget = HiddenInput()
    class Meta:
        model = Person
        # fields=['first_name', 'last_name', 'email', 'gender', 'stage', 'comorbidity', 'date_of_birth', 'weight_lbs', 'height_in', 'username','password']
        fields = '__all__'
        exclude = ['username']
        widgets = {
            'date_of_birth': DateInput(),
        }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user