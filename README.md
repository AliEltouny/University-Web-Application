# Uni Hub

**Uni Hub** is a full-stack web application for university students to manage their profiles, communities, and events. It features a Django REST API backend and a Next.js frontend, both containerized with Docker.

GitHub Repository: [https://github.com/AliEltouny/University-Web-Application](https://github.com/AliEltouny/University-Web-Application)

---

## Features

* Email registration with OTP verification
* JWT-based authentication
* User profile management
* User dashboard interface
* Responsive frontend built with modern React stack

---

## Tech Stack

### Backend

* Django 5.1.x
* Django REST Framework
* PostgreSQL
* JWT (via `djangorestframework-simplejwt`)
* Docker

### Frontend

* Next.js 15.x (TypeScript)
* React Query
* Axios
* Tailwind CSS
* Docker

---

## Project Structure

```
University-Web-Application/
├── backend/
│   ├── api/
│   ├── core/
│   ├── users/
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/
│   ├── src/
│   ├── public/
│   └── Dockerfile
└── docker-compose.yml
```

---

## Prerequisites

* [Docker](https://www.docker.com/)
* [Docker Compose](https://docs.docker.com/compose/)

---

## Run with Docker (Recommended)

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AliEltouny/University-Web-Application.git
   cd University-Web-Application
   ```

2. **Start the application using Docker Compose:**

   ```bash
   docker-compose up --build
   ```

3. **Access the services:**

   * Frontend: [http://localhost:3000](http://localhost:3000)
   * Backend API: [http://localhost:8000/api](http://localhost:8000/api)

---

## Local Development Setup (Without Docker)

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will be available at: [http://localhost:8000](http://localhost:8000)

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend will be available at: [http://localhost:3000](http://localhost:3000)

---

## API Endpoints

| Method | Endpoint                   | Description                     |
| ------ | -------------------------- | ------------------------------- |
| POST   | `/api/signup/`             | Register new user               |
| POST   | `/api/verify-otp/<email>/` | Verify OTP and activate account |
| POST   | `/api/login/`              | JWT authentication              |
| GET    | `/api/profile/`            | Retrieve user profile           |
| PATCH  | `/api/profile/`            | Update user profile             |

---

## Frontend Routes

| Route                 | Description           |
| --------------------- | --------------------- |
| `/`                   | Home page             |
| `/register`           | User registration     |
| `/verify-otp/<email>` | OTP verification page |
| `/login`              | Login page            |
| `/dashboard`          | User dashboard        |
| `/profile`            | Profile management    |

---

## License

This project is licensed under the MIT License.

---