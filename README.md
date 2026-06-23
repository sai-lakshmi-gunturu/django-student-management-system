### Django Student Management System — by Sai Lakshmi
A complete Student Management System built using Python (Django) with a clean AdminLTE UI, role‑based login, attendance tracking, and interactive dashboard charts.

This project was developed while learning Django, and the entire UI, charts, and structure have been customized to match my own design and workflow.

And if you like this project then ADD a STAR ⭐️  to this project 👆

## Features of this Project

### A. HOD / Admin
1) Dashboard with custom charts

2) Manage Staff (Add, Edit, Delete)

3) Manage Students

4) Manage Courses

5) Manage Subjects

6) Manage Sessions

7) View Attendance

8) Approve/Reject Leave

9) View & Reply to Feedback

### B. Staff
1) View dashboard with subject‑wise stats

2) Take & Update Attendance

3) Add/Update Student Results

4) Apply for Leave

5) Send Feedback

### C. Students
1) View dashboard with attendance & subject stats

2) View Attendance

3) View Results

4) Apply for Leave

5) Send Feedback


## 📸 Screenshots

Below are some key pages from the Student Management System showing the main features and UI of the application.

---

### 🔐 Login Page
This is the authentication page where Admin/HOD, Staff, and Students log in.
![Login](screenshots/login.png)

---

### 🏫 HOD Dashboard
Displays total students, staff, courses, subjects, and visual charts.
![HOD Dashboard](screenshots/hod_dashboard.png)

---

### 👨‍🏫 Staff Dashboard
Staff can take attendance, apply for leave, send feedback, and view notifications.
![Staff Dashboard](screenshots/staff_dashboard.png)

---

### 🎓 Student Dashboard
Shows attendance summary, pie chart, subject‑wise statistics, and student profile.
![Student Dashboard](screenshots/student_dashboard.png)

---

### 👥 Manage Students
Admin can add, update, delete, and view student details.
![Manage Students](screenshots/manage_students.png)

---

### 👨‍🏫 Manage Staff
Admin can add, update, delete, and view staff details.
![Manage Staff](screenshots/manage_staff.png)



## ⭐ Tech Stack
- Python

- Django

- SQLite / MySQL

- HTML, CSS, JavaScript

- AdminLTE Template

- Chart.js

## ⭐ How to Run the Project

# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/django-student-management-system.git
cd django-student-management-system

# 2. Create & activate virtual environment
Windows: 

python -m venv venv
venv\Scripts\activate

Mac:

python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver


## ⭐ Default Login Roles (if needed)
# HOD / Admin
Email: sai@gmail.com
Password: sai

# Staff(Demo)
Email: staff@gmail.com
Password: staff1

# Student(Demo)
Email: student@gmail.com
Password: student1

## ⭐ Author
# Sai Lakshmi  
Python Developer • Django Enthusiast