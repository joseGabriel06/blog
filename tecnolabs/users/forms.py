from django.contrib.auth import get_user_model
from django import forms

class SignupForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['user_type']

    def signup(self, request, user):
        user.user_type = self.cleaned_data['user_type']
        #user.last_name = self.cleaned_data['last_name']
        user.save()