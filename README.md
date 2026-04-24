# School Management System

A Django-based REST API for managing school operations including students, teachers, subjects, grades, and course assignments.

## Features

- **Student Management**: Create and list students with their grade information
- **Teacher Management**: Manage teacher profiles and assignments
- **Subject Management**: Handle academic subjects
- **Grade Management**: Organize students by grade levels
- **Course Assignments**: Assign teachers to specific subjects for particular grades
- **REST API**: Built with Django Ninja for fast, type-safe API development
- **PostgreSQL Database**: Robust data storage with relational integrity
- **Docker Support**: Easy deployment with containerization

## Tech Stack

- **Backend**: Django 5.2.12
- **API Framework**: Django Ninja 1.6.2
- **Database**: PostgreSQL
- **Containerization**: Docker & Docker Compose
- **Python**: 3.10

## Quick Start

### Prerequisites

- Docker and Docker Compose installed
- Git (optional, for cloning)

### Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd management
   ```

2. **Create Docker network** (if not exists):
   ```bash
   docker network create school_network
   ```

3. **Build and run with Docker Compose**:
   ```bash
   docker-compose up --build
   ```

The application will be available at:
- **API**: http://localhost:8000/api/
- **Admin Panel**: http://localhost:8000/admin/
- **Database**: localhost:5432 (PostgreSQL)

### Manual Installation (Development)

If you prefer to run without Docker:

1. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up PostgreSQL database** and update `management/settings.py` with your database credentials.

4. **Run migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Subjects
- `POST /api/subjects` - Create a new subject
- `GET /api/subjects` - List all subjects

### Grades
- `POST /api/grades` - Create a new grade
- `GET /api/grades` - List all grades
- `GET /api/grades/{id}` - Get grade details with assignments

### Teachers
- `POST /api/teachers` - Create a new teacher
- `GET /api/teachers` - List all teachers

### Students
- `POST /api/students` - Create a new student
- `GET /api/students` - List all students

### Course Assignments
- `POST /api/assignments` - Assign teacher to subject for a grade

## API Usage Examples

### Create a Subject
```bash
curl -X POST http://localhost:8000/api/subjects \
  -H "Content-Type: application/json" \
  -d '{"name": "Mathematics"}'
```

### Create a Grade
```bash
curl -X POST http://localhost:8000/api/grades \
  -H "Content-Type: application/json" \
  -d '{"name": "Grade 10"}'
```

### Create a Teacher
```bash
curl -X POST http://localhost:8000/api/teachers \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john.doe@school.com"}'
```

### Assign Teacher to Subject and Grade
```bash
curl -X POST http://localhost:8000/api/assignments \
  -H "Content-Type: application/json" \
  -d '{"grade_id": 1, "subject_id": 1, "teacher_id": 1}'
```

### Create a Student
```bash
curl -X POST http://localhost:8000/api/students \
  -H "Content-Type: application/json" \
  -d '{"name": "Jane Smith", "age": 16, "grade_id": 1}'
```

## Data Models

### Student
- `id`: Integer (Primary Key)
- `name`: String (max 100 chars)
- `age`: Integer
- `grade`: Foreign Key to Grade

### Teacher
- `id`: Integer (Primary Key)
- `name`: String (max 100 chars)
- `email`: Email field

### Subject
- `id`: Integer (Primary Key)
- `name`: String (max 100 chars)

### Grade
- `id`: Integer (Primary Key)
- `name`: String (max 50 chars)
- `subjects`: Many-to-Many through CourseAssignment

### CourseAssignment
- `id`: Integer (Primary Key)
- `grade`: Foreign Key to Grade
- `subject`: Foreign Key to Subject
- `teacher`: Foreign Key to Teacher
- Unique constraint on (grade, subject)

## Development

### Running Tests
```bash
python manage.py test
```

### Creating Migrations
```bash
python manage.py makemigrations student
python manage.py migrate
```

### API Documentation
Visit `http://localhost:8000/api/docs` for interactive API documentation (if Django Ninja docs are enabled).

## Deployment

### Production with Docker
```bash
docker-compose -f docker-compose.yml up -d
```

### Environment Variables
Update the following in production:
- `SECRET_KEY`: Use a secure secret key
- `DEBUG`: Set to `False`
- `ALLOWED_HOSTS`: Configure for your domain
- Database credentials in `settings.py` or environment variables

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## License

This project is licensed under the MIT License.</content>
<parameter name="filePath">/home/prabesh/pratice/management/README.md