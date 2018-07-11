from bootstrap_datepicker_plus import DatePickerInput
from django import forms
from .models import Post, LeaveApplication


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {'text': forms.Textarea(attrs={'rows':   10, 'cols': 70, 'style': 'resize:none;'})}

class PostForm(forms.ModelForm):
    class Meta:
        model = LeaveApplication
        fields = ('subject', 'text', 'from_date', 'to_date')
        widgets = {'text': forms.Textarea(attrs={'rows': 5, 'cols': 100, 'style': 'resize:none;'}),
                   'from_date': DatePickerInput(),
                   'to_date': DatePickerInput()
                   }

