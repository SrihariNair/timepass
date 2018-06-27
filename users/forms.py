import datetime

from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from django.contrib.admin import widgets
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import SelectDateWidget

from .models import CustomUser

class DateInput(forms.DateInput):
    input_type = 'date'

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        now = datetime.datetime.now()
        fields = ('username', 'email', 'gender', 'security_question', 'answer', 'birth_date',)
        widgets={
            'birth_date' :DatePickerInput(
                options={
                    'maxDate':str(datetime.datetime.now()),
                    #this needs width positioning
                }
            )
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
