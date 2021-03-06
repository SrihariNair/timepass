from django import forms
from .models import Userpost

class PostForm(forms.ModelForm):

    class Meta:
        model = Userpost
        fields = ('title', 'text')
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 25,'cols': 70,'style': 'resize:none;'
                }
            )
        }