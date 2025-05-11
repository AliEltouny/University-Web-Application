# Django Backend Setup and Troubleshooting

This guide provides step-by-step instructions to set up and run the Django backend for the UniHub platform.

---

## 1. Virtual Environment Setup

```bash
# Navigate to the project root (Example)
cd "C:/Users/Ali Eltouny/Downloads/Uni_hub"

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On macOS/Linux
# source venv/bin/activate
```

---

## 2. Install Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## 3. Database Setup

```bash
cd backend
python manage.py migrate
```

---

## 4. Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

---

## 5. Run the Development Server

```bash
python manage.py runserver 8000
```

Visit [http://localhost:8000/](http://localhost:8000/) in your browser.

---

## Troubleshooting Common Issues

### "No module named 'django'"

```bash
# Make sure the virtual environment is activated
# Then check if Django is installed
pip list | findstr Django  # Windows
# OR
pip list | grep Django     # macOS/Linux

# If not installed:
pip install django
```

---

### Database Connection Errors

* Verify database settings in `backend/settings.py`
* Make sure the database server (if external) is running
* Run `python manage.py dbshell` to test connectivity

---

### API Errors in the Frontend

* Make sure the backend is running:
  `python manage.py runserver`
* Check the frontend's API base URL
* Look for CORS errors in the browser console
* Use tools like `curl` or Postman to test endpoints

---

### Migration Issues

```bash
# Warning: This will delete all data
python manage.py flush

# Then re-create migrations
python manage.py makemigrations
python manage.py migrate
```

---

## Running Backend in Different Environments

### Development

```bash
python manage.py runserver 8000
```

### Production (with Gunicorn)

```bash
pip install gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:8000
```

---

## Enabling Debug Mode

Edit `backend/settings.py`:

```python
DEBUG = True
```

Then restart the server.

---

## Checking Logs

With the server running, view the terminal for logs or check log files if specified in `LOGGING` settings.

---

## Running Tests

```bash
python manage.py test communities
```

---

## Using Mock Mode When Backend is Unavailable

In the browser console:

```javascript
localStorage.setItem('use_mock_services', 'true')
location.reload()
```

---