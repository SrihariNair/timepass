import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import SelectDateWidget

from .models import CustomUser
from dobwidget import DateOfBirthWidget

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        now=datetime.datetime.now()
        fields = ('username', 'email', 'gender', 'security_question', 'answer', 'birth_date')
        YEARS=[x for x in range(1800,now.year )]
        widgets = {
            'birth_date': SelectDateWidget(years=YEARS),
        }



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
