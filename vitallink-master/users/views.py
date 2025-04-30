from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.db import IntegrityError  # Import this!
from .models import User, Patient, Record
from .forms import SignUpForm, UserLogin
from django.http import JsonResponse
import json

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                dob = form.cleaned_data['dob']
                gender = form.cleaned_data['gender']
                terms = form.cleaned_data['terms']

                hashed_password = make_password(password)

                user = User.objects.create(
                    username=username,
                    email=email,
                    password=hashed_password,
                    dob=dob,
                    gender=gender,
                    terms=terms,
                )
                return redirect('choose')
            except IntegrityError:  # Email already exists
                form.add_error('email', 'This email address is already in use.')
                return render(request, "users/signup.html", {"form": form})
        else:
            print(form.errors)  # Print form errors for debugging!
            # form = SignUpForm() # No need to re-initialize here
    return render(request, "users/signup.html", {"form": form})

def login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(username=username)  # Get the user by username
                if check_password(password, user.password): # Verify password
                    # Password is correct!
                    # Here you can set a session or use cookies for "logged in" state
                    request.session['user_id'] = user.id # Set a session variable
                    return redirect('choose')  # Redirect to home page
                else:
                    form.add_error(None, "Invalid username or password") # Incorrect password
            except User.DoesNotExist:
                form.add_error(None, "Invalid username or password") # Username does not exist
        else:
            print(form.errors)
    return render(request, "users/login.html", {"form": form})


def patient_information(request):
    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        contact_number = request.POST.get('contact_number')
        address = request.POST.get('address')
        profile_picture = request.FILES.get('profile_picture')

        # Save the data to the Patient model
        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            age = age,
            dob=dob,
            gender=gender,
            contact_number=contact_number,
            address=address,
            profile_picture=profile_picture,
        )
        patient.save()
        request.session['patient_id'] = patient.patient_id
        
        # Redirect to a success page or the next form
        return redirect('record_submit')  #name of view here

    return render(request, 'users/registeration/patient.html')

def record_submit(request):
    if request.method == 'POST':
        patient_id = request.session.get('patient_id')
        if not patient_id:
            return redirect('patient_information')
        
        # Get the patient object
        patient = Patient.objects.get(patient_id=patient_id)

        # Get the form data
        doc_types = request.POST.getlist('medical-doc-type[]')
        titles = request.POST.getlist('title[]')
        descriptions = request.POST.getlist('description[]')
        dates = request.POST.getlist('dod[]')
        files = request.FILES.getlist('medical-doc[]')

        # Save each record
        for doc_type, title, description, date, file in zip(doc_types, titles, descriptions, dates, files):
            record = Record(
                patient=patient,
                document_type=doc_type,
                title=title,
                description=description,
                date=date,
                file=file,
            )
            record.save()

        return redirect('patient_profile', patient_id=patient_id)  # Redirect to a success page

    return render(request, 'users/registeration/pnext.html')

def patient_profile(request, patient_id):
    patient = get_object_or_404(Patient, patient_id=patient_id)
    return render(request, 'users/dashboards/pd.html', {'patient': patient})

def filter_records(request):
    if request.method == 'GET':
        patient_id = request.GET.get('patient_id')
        record_type = request.GET.get('type')
        
        patient = get_object_or_404(Patient, patient_id=patient_id)
        records = patient.records.filter(document_type=record_type)
        
        records_data = []
        for record in records:
            records_data.append({
                'title': record.title,
                'description': record.description,
                'date': record.date.strftime('%Y-%m-%d'),
                'file': record.file.url
            })
        
        return JsonResponse({'records': records_data})

def DoctorReg(request):
    return render(request,'users/registeration/doctor-registeration.html', {})