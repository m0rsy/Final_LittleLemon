# 🍋 Little Lemon Restaurant — Back-End Capstone Project

A full-stack back-end web application built with **Django** and **MySQL** as the capstone project of the **Meta Back-End Developer Professional Certificate** on Coursera.

---

## 📌 Project Overview

Little Lemon is a restaurant web application that demonstrates core back-end development skills, including REST API design, database integration, user authentication, and unit testing. The project was built to simulate a real-world back-end system for a restaurant that handles menu browsing and table reservations.

---

## 🚀 Features

- 🍽️ **Menu API** — Browse and manage restaurant menu items
- 📅 **Table Booking API** — Reserve and manage table bookings
- 🔐 **User Registration & Authentication** — Secure user sign-up and login using Django's built-in auth system
- 🖥️ **Django Template System** — Dynamic HTML pages served via Django views
- 🧪 **Unit Testing** — Tested API endpoints with Django's test framework and Insomnia
- 🗄️ **MySQL Database** — Persistent data storage connected via Django ORM
- 📁 **Version Control** — Full Git history with clean, structured commits

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| Back-End Framework | Django |
| API | Django REST Framework |
| Database | MySQL |
| Authentication | Django Auth |
| Testing | Django Unit Tests, Insomnia |
| Version Control | Git & GitHub |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.x
- MySQL
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/Yousef-maged/final_littlelemon.git
cd final_littlelemon

# 2. Create and activate a virtual environment
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your MySQL database in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# 5. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 6. Create a superuser (optional)
python manage.py createsuperuser

# 7. Run the development server
python manage.py runserver
```

---

## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/menu/` | List all menu items |
| GET | `/api/menu/<id>/` | Get a single menu item |
| POST | `/api/menu/` | Add a new menu item |
| GET | `/api/bookings/` | List all table bookings |
| POST | `/api/bookings/` | Create a new booking |
| POST | `/auth/users/` | Register a new user |
| POST | `/auth/token/login/` | Obtain auth token |

---

## 🧪 Running Tests

```bash
python manage.py test
```

API endpoints were also tested manually using **Insomnia**.

---

## 📜 Certificate

This project was built as part of the **Meta Back-End Developer Professional Certificate** (9 Courses) on Coursera.

🔗 [Verify Certificate](https://coursera.org/verify/professional-cert/P0X9YPCQ219T)

---

## 👤 Author

**Youssef Maged Makram**
- GitHub: [github.com/Yousef-maged](https://github.com/Yousef-maged)
- LinkedIn: [linkedin.com/in/youssef-maged-582065287](https://www.linkedin.com/in/youssef-maged-582065287/)
