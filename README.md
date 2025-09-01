# 🐍 Lybra-API
This repository contains the backend of the Lybra, a modern library management system featuring subscriptions, borrowings, gamification, and personalized recommendations.

---
## 🎯 Project Context

This project is developed as part of my full-stack developer training at **Technofuturtic** (Python/Angular).  
The goal is to deliver a **Minimum Viable Product (MVP)** within **2 weeks**, showcasing backend architecture and API design.

- Backend: Python 3.13, Django REST Framework
- Frontend: Angular 20 (link to frontend repo coming soon)

> 🧠 MVP Scope: Focused on **library management** (admin/staff side).  
> Future versions will include **user-facing features** (catalog browsing, borrowing, recommendations, gamification).

---
## 🚀 MVP Scope

The MVP focuses on the following core apps:

- `auth`: Authentication and roles
- `users`: User profiles
- `books`: Book catalog
- `borrowings`: Borrowing and reservations
- `subscriptions`: Subscriptions and payments
- `cart`: Borrowing cart
- `configuration`: Global settings

Additional apps such as `gamification` and `recommendation` are planned as bonus features if time allows.

---
## 🧱 Project Structure

```
lybra-API/
├── apps/
│   ├── auth/
│   ├── users/
│   ├── books/
│   ├── borrowings/
│   ├── subscriptions/
│   ├── cart/
│   ├── gamification/
│   ├── recommendation/
│   ├── configuration/
├── core/
├── shared/
├── manage.py
├── .env.example
└── requirements/
    ├── base.txt
    ├── dev.txt
    └── prod.txt
```

---
## 🧠 Architecture Overview

The backend follows a clean architecture:

- View → Service → ORM
- Business logic is isolated in `services/`
- Views use either `ModelViewSet` with method overrides or `GenericAPIView` + mixins
- Repositories are used only when queries are complex or reused

---
## 🛠️ Technologies

- Python 3.13
- Django & Django REST Framework
- PostgreSQL
- drf-spectacular

---
## 📖 API Documentation

The API is documented using **drf-spectacular**.  
[Link**]

---
## ⚙️ Setup Instructions

	# Install dependencies
	pip install -r requirements/dev.txt
	
	# Run migrations
	python manage.py migrate
	
	# Start development server
	python manage.py runserver



###