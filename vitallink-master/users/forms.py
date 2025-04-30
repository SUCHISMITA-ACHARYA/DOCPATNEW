from django import forms
from .models import User, Patient

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=255)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, error_messages={'min_length': 'Password must be at least 8 characters long.'})
    cpassword = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'dob', 'gender', 'terms')  # Include all fields

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        cpassword = cleaned_data.get("cpassword")

        if password != cpassword:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data


class UserLogin(forms.Form):
    username = forms.CharField(max_length=150)  # Or email, depending on your setup
    password = forms.CharField(widget=forms.PasswordInput)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'gender', 'contact_number', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 4}),
        }