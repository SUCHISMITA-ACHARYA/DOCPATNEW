from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255)  # Adjust max_length as needed
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed password here
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ])
    terms = models.BooleanField()  # For Terms and Conditions

    def __str__(self):
        return self.username  # Or fullname, or a combination
    
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other'),
        ],
    )
    contact_number = models.CharField(max_length=20)
    address = models.TextField()
    profile_picture = models.ImageField(
        upload_to='users/UserData/Profile_Pictures/',  # Files will be uploaded to the 'profile_pictures/' directory
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])],  # Allowed file types
    )
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Record(models.Model):
    # Dropdown choices for the type of document
    DOCUMENT_TYPES = [
        ('prescription', 'Prescription'),
        ('xray', 'X-ray'),
        ('scan', 'Scan'),
        ('report', 'Report'),
        ('document', 'Document'),
    ]
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='records')
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()

    file = models.FileField(
        upload_to='records/',  # Files will be uploaded to the 'records/' directory
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'jpeg', 'png'])],  # Allowed file types
        blank=True,  # Optional field
        null=True,   # Optional field
    )

    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES,
        default='document',  # Default value
    )

    def __str__(self):
        return f"{self.title} ({self.get_document_type_display()})"