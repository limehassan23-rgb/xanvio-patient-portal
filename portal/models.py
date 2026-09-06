from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)

    def __clstr__(self):
        return self.name

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField() # Date of Birth
    phone = models.CharField(max_length=15)
    # ... any other patient fields you already have ...

    def __str__(self):
        return self.name

# --- OPTION 1: THE APPOINTMENT ---
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateTimeField()
    service = models.CharField(max_length=100) # e.g., Blood Draw, COVID Test
    status = models.CharField(max_length=20, default="Scheduled")

    def __str__(self):
        return f"{self.service} for {self.patient.name}"

# --- OPTION 2: THE LAB RESULT ---
class LabResult(models.Model):
    # This links the result to the specific appointment
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=100)
    result_value = models.CharField(max_length=100)
    date_tested = models.DateField()
    status = models.CharField(max_length=20, default="Final")
    
    # Adding this makes it "Pro" - you can upload a PDF
    report_file = models.FileField(upload_to='lab_reports/', null=True, blank=True)

    def __str__(self):
        return f"{self.test_name} - {self.patient.name}"