from django import forms
from .models import Appointment

class AppointmentBookingForm(forms.ModelForm):
    # We define the dropdown options here for your lab services
    SERVICE_CHOICES = [
        ('Toxicology Screen', 'Toxicology Screen / Drug Testing'),
        ('Blood Draw', 'Routine Blood Draw'),
        ('COVID-19 PCR', 'COVID-19 PCR Test'),
        ('Urinalysis', 'Urinalysis'),
    ]

    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Appointment
        fields = ['service', 'date']
        widgets = {
            # This forces the browser to open a modern date-time calendar picker
            'date': forms.DateTimeInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'}
            ),
        }