# Threat Detection System

A Django REST Framework-based threat detection and alerting system with JWT authentication.

## Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.11+** (Python 3.11 is used in Docker)
- **PostgreSQL 15+** (if running locally without Docker)
- **pip** (Python package manager)
- **Docker and Docker Compose** (optional, for containerized setup)
- **Git** (for cloning the repository)

## Project Structure

```
cyethack/
├── cyethack/          # Django project settings
│   ├── settings.py    # Main settings file
│   ├── urls.py        # Root URL configuration
│   └── ...
├── threat/            # Main application
│   ├── models.py      # User, Event, Alert models
│   ├── views.py       # API views
│   ├── serializers.py # DRF serializers
│   ├── urls.py        # API endpoints
│   └── ...
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
├── dockerfile         # Docker image configuration
├── docker-compose.yml # Docker Compose configuration
└── db.sqlite3         # SQLite database (if used)
```

## Setup Instructions

### Option 1: Local Setup (Without Docker)

#### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd threat-detection/cyethack
```

#### Step 2: Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

#### Step 4: Set Up PostgreSQL Database

1. Install PostgreSQL if not already installed
2. Create a new database:

```bash
# Connect to PostgreSQL
psql -U postgres

# Create database
CREATE DATABASE postgres;

# Exit psql
\q
```

3. Update database credentials in `cyethack/settings.py` if needed:
   - Database name: `postgres`
   - User: `postgres`
   - Password: `postgres`
   - Host: `localhost`
   - Port: `5432`

#### Step 5: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

#### Step 6: Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin user.

#### Step 7: Run the Development Server

```bash
python manage.py runserver
```

The server will be available at `http://127.0.0.1:8000/`

### Option 2: Docker Setup (Recommended)

#### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd threat-detection/cyethack
```

#### Step 2: Build and Run with Docker Compose

```bash
docker-compose up --build
```

This will:
- Build the Django application container
- Start PostgreSQL database container
- Run migrations automatically
- Start the Django development server on port 8000

#### Step 3: Create Superuser (in a new terminal)

```bash
docker-compose exec web python manage.py createsuperuser
```

#### Step 4: Access the Application

- API: `http://localhost:8000/api/`
- Admin Panel: `http://localhost:8000/admin/`

#### Useful Docker Commands

```bash
# Stop containers
docker-compose down

# Stop and remove volumes (clears database)
docker-compose down -v

# View logs
docker-compose logs -f

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser

# Access Django shell
docker-compose exec web python manage.py shell
```

## API Endpoints

The API is available at `http://localhost:8000/api/`

### Authentication Endpoints

- **POST** `/api/auth/` - Obtain JWT token pair (access + refresh)
  - Body: `{"username": "your_username", "password": "your_password"}`
  
- **POST** `/api/auth/refresh/` - Refresh access token
  - Body: `{"refresh": "your_refresh_token"}`
  
- **POST** `/api/auth/logout/` - Blacklist refresh token
  - Body: `{"refresh": "your_refresh_token"}`

### User Endpoints

- **GET** `/api/users/` - List all users (requires authentication)
- **GET** `/api/users/<uuid:id>/` - Get user details (requires authentication)

### Event Endpoints

- **GET** `/api/events/` - List all events (requires authentication)
- **POST** `/api/events/` - Create new event (requires authentication)
- **GET** `/api/events/<uuid:id>/` - Get event details (requires authentication)
- **PUT/PATCH** `/api/events/<uuid:id>/` - Update event (requires authentication)
- **DELETE** `/api/events/<uuid:id>/` - Delete event (requires authentication)

### Alert Endpoints

- **GET** `/api/alerts/` - List all alerts (requires authentication)
- **POST** `/api/alerts/` - Create new alert (requires authentication)
- **GET** `/api/alerts/<uuid:id>/` - Get alert details (requires authentication)
- **PUT/PATCH** `/api/alerts/<uuid:id>/` - Update alert (requires authentication)
- **DELETE** `/api/alerts/<uuid:id>/` - Delete alert (requires authentication)

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. To access protected endpoints:

1. Obtain a token pair from `/api/auth/`:
```bash
curl -X POST http://localhost:8000/api/auth/ \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username", "password": "your_password"}'
```

2. Use the access token in subsequent requests:
```bash
curl -X GET http://localhost:8000/api/events/ \
  -H "Authorization: Bearer <your_access_token>"
```

## Database Models

### User
- Custom user model extending AbstractUser
- Fields: email, first_name, last_name, role (admin/analyst)
- Uses UUID as primary key

### Event
- Represents security events/threats
- Fields: source, event_type, severity (low/medium/high/critical), description
- Uses UUID as primary key

### Alert
- One-to-one relationship with Event
- Fields: event, status (open/acknowledged/resolved)
- Uses UUID as primary key

## Dependencies

- **Django 5.2.9** - Web framework
- **djangorestframework 3.16.1** - REST API framework
- **djangorestframework-simplejwt 5.5.1** - JWT authentication
- **django-filter 22.1** - Filtering support
- **psycopg2-binary 2.9.11** - PostgreSQL adapter

## Development

### Running Tests

```bash
# Local
python manage.py test

# Docker
docker-compose exec web python manage.py test
```

### Making Migrations

```bash
# Local
python manage.py makemigrations
python manage.py migrate

# Docker
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
```

### Django Admin

Access the admin panel at `http://localhost:8000/admin/` using your superuser credentials.

## Troubleshooting

### Database Connection Issues

If you encounter database connection errors:

1. **Local Setup**: Ensure PostgreSQL is running and credentials in `settings.py` are correct
2. **Docker Setup**: Ensure the database container is running:
   ```bash
   docker-compose ps
   ```

### Port Already in Use

If port 8000 is already in use:

1. **Local**: Change the port:
   ```bash
   python manage.py runserver 8001
   ```

2. **Docker**: Update the port mapping in `docker-compose.yml`:
   ```yaml
   ports:
     - "8001:8000"
   ```

### Migration Issues

If migrations fail:

```bash
# Reset migrations (WARNING: This will delete data)
python manage.py migrate threat zero
python manage.py migrate
```

## Environment Variables

For production, consider using environment variables for sensitive settings:

- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (set to False in production)
- `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD`, `DATABASE_HOST`, `DATABASE_PORT`

## License

[Add your license information here]

## Contributing

[Add contributing guidelines here]

