from django.shortcuts import render, redirect
from .models import Patient, Appointment, LabResult
from .forms import AppointmentBookingForm

# =========================================================
# 1. THE SEARCH PAGE VIEW
# =========================================================
def search_page(request):
    results = None
    appointments = None
    patient = None
    error = None

    if request.method == "POST":
        name = request.POST.get('name')
        dob = request.POST.get('dob')

        if name and dob:
            try:
                # Find the patient by name (case-insensitive) and DOB
                patient = Patient.objects.get(name__iexact=name, dob=dob)
                
                # Get all Lab Results linked to this patient
                results = LabResult.objects.filter(patient=patient).order_by('-date_tested')
                
                # Get all Appointments linked to this patient
                appointments = Appointment.objects.filter(patient=patient).order_by('-date')

            except Patient.DoesNotExist:
                error = "No patient record found with that Name and Date of Birth."
            except Exception as e:
                error = f"An unexpected error occurred: {e}"
        else:
            error = "Please provide both Name and Date of Birth."

    return render(request, 'search.html', {
        'patient': patient,
        'results': results,
        'appointments': appointments,
        'error': error
    })


# =========================================================
# 2. THE APPOINTMENT BOOKING VIEW
# =========================================================
def book_appointment(request):
    form = AppointmentBookingForm()
    success_message = None

    if request.method == "POST":
        form = AppointmentBookingForm(request.POST)
        patient_name = request.POST.get('patient_name')
        patient_dob = request.POST.get('patient_dob')

        if form.is_valid() and patient_name and patient_dob:
            try:
                # Match the booking to an existing patient in your database
                patient = Patient.objects.get(name__iexact=patient_name, dob=patient_dob)
                
                # Save the appointment form data but don't commit to DB yet
                appointment = form.save(commit=False)
                
                # Attach the found patient to the appointment object
                appointment.patient = patient
                appointment.status = "Scheduled"
                appointment.save()

                success_message = f"Appointment successfully scheduled for {patient.name}!"
                form = AppointmentBookingForm() # Reset the form after success
                
            except Patient.DoesNotExist:
                form.add_error(None, "Could not book: No patient profile found matching that Name and DOB. Please create a patient record first.")

    return render(request, 'book_appointment.html', {
        'form': form,
        'success_message': success_message
    })


# =========================================================
# 3. THE ADMIN NOTIFICATION VIEW
# =========================================================
def admin_notifications(request):
    unread_notifications = Appointment.objects.filter(is_read=False).order_by('-date')
    unread_count = unread_notifications.count()

    if request.method == "POST":
        unread_notifications.update(is_read=True)
        return redirect('admin_notifications')

    return render(request, 'admin_notifications.html', {
        'notifications': unread_notifications,
        'count': unread_count
    })