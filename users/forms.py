import datetime

from bootstrap_datepicker_plus import DatePickerInput
from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import CustomUser, Documents


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        now = datetime.datetime.now()
        fields = ('username', 'email', 'gender', 'security_question', 'answer', 'birth_date')
        widgets={
            'birth_date' :DatePickerInput(
                options={
                    'maxDate':str(datetime.datetime.now()),
                }
            )
        }
        help_texts={
            'email':'Enter valid email address',
        }


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class DocumentListForm(forms.ModelForm):
    class Meta:
         model = Documents
         fields = ('resume')