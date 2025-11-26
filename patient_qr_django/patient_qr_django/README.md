# Django Patient QR Code System

A simple Django application where patients are registered and automatically get QR codes generated.

## 🚀 Quick Start

### Step 1: Navigate to the project folder
```bash
cd c:\Users\Devanarayan\Desktop\111\patient_qr_django
```

### Step 2: Create a superuser (admin account)
```bash
python manage.py createsuperuser
```
- Enter username (e.g., `admin`)
- Enter email (optional, can press Enter to skip)
- Enter password (e.g., `admin123`)

###Step 3: Start the server
```bash
python manage.py runserver
```

### Step 4: Access the system

**Patient List Page:** http://127.0.0.1:8000/
- View all registered patients
- Click on any patient to see their QR code

**Admin Panel:** http://127.0.0.1:8000/admin/
- Login with your superuser credentials
- Click "Patients" → "Add Patient"
- Fill in patient details (QR code auto-generates!)

## ✨ Features

- ✅ **Auto Patient ID Generation** - Unique IDs like PAT00123
- ✅ **Auto QR Code Generation** - Created automatically on save
- ✅ **Beautiful Admin Interface** - QR codes visible in admin
- ✅ **Patient List Page** - Modern card-based layout
- ✅ **QR Code Display Page** - Large QR code with download button
- ✅ **Download QR Codes** - Save as PNG images

## 📋 How to Add a Patient

1. Go to: http://127.0.0.1:8000/admin/
2. Login with superuser credentials
3. Click "Patients" → "+ Add Patient"
4. Fill in:
   - Name (required)
   - Age (required)
   - Phone (required)
   - Blood Group (optional)
5. Click "Save"
6. QR code generates automatically! ✨

## 📱 How QR Codes Work

Each QR code contains:
- Patient ID
- Name
- Age
- Phone number
- Blood Group

Scan with any smartphone camera to view patient info instantly!

## 🗂️ Project Structure

```
patient_qr_django/
├── manage.py                    # Django management
├── db.sqlite3                   # Database
├── media/qr_codes/              # Generated QR codes
├── patient_qr_django/
│   ├── settings.py              # Configuration
│   └── urls.py                  # URL routing
└── patients/
    ├── models.py                # Patient model with QR generation
    ├── admin.py                 # Admin interface
    ├── views.py                 # Views for patient list and QR display
    ├── urls.py                  # Patient app URLs
    └── templates/patients/
        ├── patient_list.html    # Patient list page
        └── patient_qr.html      # QR code display page
```

## 🛠️ Tech Stack

- **Framework:** Django 4.2+
- **Database:** SQLite3
- **QR Generation:** qrcode library with Pillow
- **Frontend:** HTML5 + CSS3 (modern gradients)

## 📝 Database Schema

**Patient Model:**
- `patient_id` - Auto-generated unique ID (PAT + 5 digits)
- `name` - Patient name
- `age` - Patient age
- `phone` - Contact number
- `blood_group` - Blood type (optional)
- `qr_code` - QR code image (auto-generated)
- `created_at` - Registration date
- `updated_at` - Last update

---

**Enjoy your simple Django Patient QR System!** 🎉

For questions or issues, check the Django documentation: https://docs.djangoproject.com/
