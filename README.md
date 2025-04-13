# 🛒 E-Commerce Backend API with FastAPI

This is a fully functional backend for an E-commerce platform built with **FastAPI**, **SQLAlchemy**, and **JWT Authentication**.

## 🚀 Features

- 🔐 User Registration & Login with JWT
- 👤 User Authentication Middleware (applied globally except login/register)
- 🛆 Product Management (CRUD)
- 🏷 Category Management (CRUD)
- 🧾 Order Handling (optional future scope)
- 📄 Swagger API Docs (auto-generated)

---

## ⚙️ Tech Stack

- **FastAPI** – modern, high-performance API framework
- **SQLAlchemy** – ORM for database
- **SQLite / PostgreSQL** – database (configurable)
- **JWT (python-jose)** – for secure authentication
- **Passlib (bcrypt)** – for password hashing

---

## 🧪 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ecommerce-fastapi.git
cd ecommerce-fastapi
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
uvicorn app.main:app --reload
```

---

## 🔑 Authentication

- Token is returned on `/auth/login` using `Bearer <token>`
- Include token in **Authorization header** for protected routes

> **Example:**
```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
```

---

## 📚 API Documentation

FastAPI automatically provides Swagger UI at:

- [`/docs`](http://localhost:8000/docs)
- [`/redoc`](http://localhost:8000/redoc)

---

## 📦 Future Enhancements

- 🛒 Cart & Order APIs
- 🧾 Payment Gateway Integration
- 📊 Admin Dashboard Support
- 📧 Email verification & password reset

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit a PR.

---

## 📜 License

This project is licensed under the **MIT License**.

