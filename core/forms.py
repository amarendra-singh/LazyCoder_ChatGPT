from django import forms
from . models import User  

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model=User
        fields=['username','firstname','lastname','email','password' ]

    #     widgets = {
    #         for i in fields:
    #             i : forms.TextInput(attrs={'class': 'fieldcss'})
    #    }

        # def __init__(self, *args, **kwargs):
        #     super().__init__(*args, **kwargs)
        #     self.helper.form_class = 'fieldcss'

    def clean(self):
        cleaned_data=super(UserForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password does not match")