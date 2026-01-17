from django import forms
from .models import BloodRequest
from django.utils import timezone
from datetime import date


class BloodRequestForm(forms.ModelForm):
    class Meta:
        model = BloodRequest
        fields = ['patient_name', 'required_blood_group', 'number_of_bags', 
                 'hospital_name', 'hospital_address', 'patient_condition', 'emergency_level', 
                 'required_date', 'contact_phone', 'additional_info']
        
        widgets = {
            'patient_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'required_blood_group': forms.Select(attrs={
                'class': 'form-control'
            }),
            'number_of_bags': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1',
                'value': '1'
            }),
            'hospital_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital name'
            }),
            'hospital_address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter hospital address',
                'rows': 3
            }),
            'patient_condition': forms.Select(attrs={
                'class': 'form-control'
            }),
            'emergency_level': forms.Select(attrs={
                'class': 'form-control'
            }),
            'required_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'contact_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter contact phone number'
            }),
            'additional_info': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Additional information (optional)',
                'rows': 3,
                'required': False
            }),
        }
    
    def clean_required_date(self):
        required_date = self.cleaned_data.get('required_date')
        if required_date:
            if required_date < date.today():
                raise forms.ValidationError('Required date cannot be in the past.')
        return required_date