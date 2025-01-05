from django import forms
from .models import *

class WorkProgressForm(forms.ModelForm):
    class Meta:
        model = WorkProgress
        fields = ['name_of_site','location','name_of_the_employee', 'phone_number','to_day_expensives', 'description']

        # Add custom widgets for the fields
        widgets = {
            'name_of_site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site Location name'}),
            'name_of_the_employee': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter employee name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'to_day_expensives': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter today\'s expenses'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }




from django import forms
from .models import Employee

class EmployeeLoginForm(forms.Form):
    mobile_number = forms.CharField(max_length=15, label='Mobile Number')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')



class WorkProgresForm(forms.ModelForm):
    class Meta:
        model = WorkProgress
        fields = ['name_of_site','location','name_of_the_employee', 'phone_number','to_day_expensives', 'description']

        # Add custom widgets for the fields
        widgets = {
            'name_of_site': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter site Location name'}),
            'name_of_the_employee': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter employee name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'to_day_expensives': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter today\'s expenses'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description', 'rows': 4}),
        }



class ContactDealForm(forms.ModelForm):
    class Meta:
        model = contract_deal
        fields = ['name', 'phone_number', 'contract_deal', 'location', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }

    # Custom validation for the name field
    def clean_name(self):
        name = self.cleaned_data.get('name')
        # You can add more custom validation logic here if necessary
        return name

    # Custom validation for the phone_number field
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        # You can add more custom validation logic here if necessary
        return phone_number



