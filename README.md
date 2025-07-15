# 🏥 Vital Link – Patient-Doctor Healthcare Web Platform

Vital Link is a full-stack web application that enables patients to securely store medical records, search for doctors by specialty, and receive timely reminders for vaccinations and medications. Doctors can access patient data only when permitted, creating a trusted, private, and collaborative healthcare experience.

---

## 📌 Features

- 🔐 **Role-Based Authentication** – Separate logins for Patients and Doctors.
- 📁 **Medical Record Management** – Patients can upload and manage their health records.
- 🧑‍⚕️ **Doctor Directory Search** – Patients can search for specialists and view profiles.
- 📲 **Twilio-Powered Reminders** – SMS notifications for medications and age-based vaccinations.
- ✅ **Access Control** – Doctors can only view records if granted access by the patient.

---

## 🧱 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Django (Python)
- **Database:** MySQL / SQLite
- **Notifications:** Twilio API (SMS)

---

## 🖥️ Project Structure
vital_link/ <br>
│<br>
├── patients/ # Patient-specific views, models, and forms <br>
├── doctors/ # Doctor-specific access and features <br>
├── records/ # Medical record upload and retrieval <br>
├── reminders/ # Logic for vaccination and medication alerts <br>
├── templates/ # HTML templates for all pages <br>
├── static/ # CSS and JS files <br>
├── db.sqlite3 # Database <br>
└── manage.py <br>

---

## 📸 Sample Screenshots

### Home Page
<img width="1920" height="1080" alt="homepage" src="https://github.com/user-attachments/assets/d9503547-25d9-4426-8670-418c2c512770" />

### Site Login Page
<img width="1920" height="1080" alt="Screenshot (126)" src="https://github.com/user-attachments/assets/6dea201e-f67c-43e6-a8e0-19207dcd98c8" />

### Type of Login Page
<img width="1920" height="1080" alt="typeoflogin" src="https://github.com/user-attachments/assets/51b0a383-457b-4555-a962-a4ab576828f9" />

### Doctor and Patient Signup Page
<img width="1920" height="1080" alt="patientregisteration" src="https://github.com/user-attachments/assets/d8de6607-7f89-42be-b99c-ef80d9f70ff6" />
<img width="1920" height="1080" alt="drlogin" src="https://github.com/user-attachments/assets/ca3c55da-f2ad-408a-8959-fd3b82e21534" />

### Vacination Schedule Page
<img width="1920" height="1080" alt="vaccination schedule" src="https://github.com/user-attachments/assets/be54d147-f942-4bb2-bd7d-eac769aec98d" />
<img width="1920" height="1080" alt="vacination schedule" src="https://github.com/user-attachments/assets/4b8be99b-7fe0-4ae6-aa89-64748db61a9c" />

---

## 🧪 How to Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/vital-link.git
   cd vital-link
   python manage.py migrate
   python manage.py runserver

---

## 🚀 Future Enhancements
✅ Email-based reminders in addition to SMS

🗂️ Record categorization by illness/type

📊 Health analytics and trend tracking

🔐 Two-factor authentication for login

---

# 🧑‍💻 Authors
PRAVEEN KUMAR R K : https://github.com/Praveen-Kumar-RK <br>
SUCHISMITA ACHARYA : https://github.com/SUCHISMITA-ACHARYA <br>
JISHNU BHARGAV M : https://github.com/jishnu019-coder

---
Refer Report.pdf for further information
