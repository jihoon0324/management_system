from django import forms

from .models import Staff



class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_number' , 'day_of_employment','first_name' , 'last_name','email' , 'position', 'gender']
        labels={
            'staff_number' :'Staff Number',
            'day_of_employment': 'Day of Employment',
            'first_name' : 'First Name',
            'last_name' : 'Last Name',
            'email'  : 'Email',
            'position': 'Position',

            'gender' : 'Gender'
        }
        GENDER_CHOICES = (
            ('' , 'Select Gender'),
            ('M', 'Male'),
            ('F', 'Female'),
        )
        POSITION_CHOICES ={
            ('' , 'Select Positon'),
            ('1', 'Chief executive officer (CEO)'),
            ('2', 'Chief operating officer '),
            ('3', ' Chief information officer'),
            ('4', ' Chief financial officer '),


        }

        widgets={
            'student_number': forms.NumberInput(attrs={'class':'form-control'}),
            'day_of_employment': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'position': forms.Select(choices=POSITION_CHOICES,attrs={'class': 'form-control'}),
             'gender': forms.Select(choices=GENDER_CHOICES,attrs={'class': 'form-control'}),


        }
