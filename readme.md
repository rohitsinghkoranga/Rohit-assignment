# Crego — Transactions CRUD + Redis Request Counter
# Django Assignment

This project is a Django-based web application demonstrating API development using the **Django REST Framework (DRF)**, **PostgreSQL** as the database, and **Redis** for caching or middleware functionality.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/rohitsinghkoranga/rohit-assignment.git
cd rohit-assignment

## Tech
- Django, DRF
- PostgreSQL
- Redis
- python-dotenv

2.⁠ ⁠Create a Virtual Environment

It's always good practice to isolate your Django project dependencies.

python3 -m venv venv
source venv/bin/activate   # On macOS/Linux

3.⁠ ⁠Install Dependencies

pip install -r requirements.txt

4.⁠ ⁠Setup PostgreSQL Database

# Create a new PostgreSQL database
CREATE DATABASE your_db_name;

# Update settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5.⁠ ⁠Apply Migrations

python manage.py makemigrations
python manage.py migrate

6.⁠ ⁠Create a Superuser

python manage.py createsuperuser

7.⁠ ⁠Run the Development Server

python manage.py runserver

8.⁠ ⁠Start Redis Server

# macOS
brew services start redis

# Linux
sudo systemctl start redis

# Windows
redis-server

Check if Redis is running:

redis-cli ping

If it returns PONG, Redis is working correctly.

How to Run the Server

source venv/bin/activate
python manage.py runserver

Then open your browser and go to: http://127.0.0.1:8000/

How to Start Redis

brew services start redis        # macOS
sudo systemctl start redis       # Linux
redis-server                     # Windows

Short Note: How My Middleware Works

In my Django project, I created a custom middleware called RequestCounterMiddleware that uses Redis to count how many times the APIs are accessed.

Every time a user sends any request to the Django application, this middleware runs before and after the view is processed. Inside it, I connect to Redis and call the incr() function on a key named "api_request_count". This automatically increases the counter value by 1 for every incoming request.

By doing this, Redis keeps a real-time count of the total API requests without slowing down the server, since Redis stores data in memory and is very fast.

Later, my stats_view reads this Redis key and displays the total number of requests along with the total number of transactions stored in the database.


---

In simple terms

The middleware runs for every request.

It connects to Redis using the redis library.

It increases the counter api_request_count by 1 each time.

The stats API then retrieves this count and shows it to the user.


 Example flow:

1. User calls /api/transactions/ → middleware runs → Redis count +1


2. User calls /api/stats/ → middleware runs → Redis count +1 → stats view fetches count → returns JSON like:

{"total_requests": 7, "total_transactions": 3}

    