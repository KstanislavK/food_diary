from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import FoodIntake


class FoodIntakeCRUDForm(forms.ModelForm):
    class Meta:
        model = FoodIntake
        exclude = ('pk', 'user')

    def __init__(self, *args, **kwargs):
        super(FoodIntakeCRUDForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class SearchForm(forms.Form):
    pass


class UserRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
