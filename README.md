# Agricultural Calendar

This repository contains an agricultural calendar that helps users plan and manage their crops. The project includes a Django backend for server-side logic and a Vue.js frontend for a responsive user interface.

## Project Objectives
- Provide a user-friendly calendar to schedule and track crop activities.
- Enable users to view, add, and manage their agricultural tasks.
- Deliver a responsive and modern web application.

## Directory Structure

Below is the high-level directory layout of the project:

```
Agricultural-Calendar/
├── backend/                      # Django backend
│   ├── core/                     # Project settings, URLs, and configurations
│   ├── calendario/               # Django app: models, views, serializers, migrations
│   ├── membros/                  # Authentication directory
│   ├── db.sqlite3                # SQLite database file
│   ├── manage.py                 # Django management script
│   └── requirements.txt          # Python dependencies
│
├── frontend/                     # Vue.js frontend
│   ├── public/                   # Static files and index.html
│   ├── src/
│   │   ├── assets/               # Fonts, CSS, images, etc.
│   │   ├── components/           # Vue.js components
│   │   └── main.js               # Application entry point
│   ├── package.json              # NPM dependencies and scripts
│   ├── vite.config.js            # Vite build configuration
│   └── .gitignore                # Frontend-specific ignores
│
├── docs/                         # Documentation and guidelines
└── tests/                        # Test cases for the application
```

## Getting Started

### Prerequisites
- Python 3 and pip installed (for backend)
- Node.js and npm installed (for frontend)

### Backend Setup (Django)
1. **Navigate to the backend directory:**
    ```bash
    cd backend
    ```
2. **Create and activate a virtual environment:**
    - On macOS/Linux:
      ```bash
      python3 -m venv venv
      source venv/bin/activate
      ```
    - On Windows:
      ```bash
      python -m venv venv
      venv\Scripts\activate
      ```
3. **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Apply migrations and set up the database:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Run the Django server:**
    ```bash
    python manage.py runserver
    ```
    The backend will be accessible at http://127.0.0.1:8000/.

### Frontend Setup (Vue.js)
1. **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```
2. **Install Node dependencies:**
    ```bash
    npm install
    ```
3. **Run the development server:**
    ```bash
    npm run dev
    ```
    The frontend will be available at the local address provided by Vite (typically http://localhost:3000 or similar).

## Additional Information
- **API Endpoints:** The Django backend provides endpoints for managing crop events, schedules, and user profiles.
- **CORS:** The backend is configured to allow requests from both the frontend and development origins.
- **Contribution:** Contributions are welcome! Please review the guidelines in the docs before submitting pull requests.
- **License:** Distributed under the MIT License; see the `LICENSE` file for more details.

Happy farming and efficient crop management!