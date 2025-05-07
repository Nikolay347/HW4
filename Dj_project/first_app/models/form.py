from django import forms
from .student import Student


class StudentAdminForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        input_formats=['%Y-%m-%d'],
        required=False,
        label='Birth date (YYYY-MM-DD)'
    )

    class Meta:
        model = Student
        fields = '__all__'