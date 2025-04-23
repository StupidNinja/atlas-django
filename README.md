# To-Do List Application

This is a simple to-do list application built with Django and Django REST Framework. It includes JWT authorization for user authentication.

## Project members

 - Almasbekov Damir

 - Zhamshid Kabanbay

 - Temirkhan Adilet

## Project Structure

```
atlas-django/
├── manage.py
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── todos/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd todo_project
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## Usage

- Access the API at `http://127.0.0.1:8000/api/`.
- Use JWT for authentication. Obtain a token by sending a POST request to `/api/token/` with your username and password.


## For Frontend Developers

### API Base URL

- The backend API is available at: `http://127.0.0.1:8000/api/`

### Authentication

- This project uses **JWT (JSON Web Token)** authentication.
- To authenticate, obtain a token by sending a POST request to the login endpoint (e.g., `/api/users/login/`) with your username and password.
- Include the received access token in the `Authorization` header for all protected requests:

  ```
  Authorization: Bearer <your_access_token>
  ```

### CORS

- CORS is enabled for local development. If your frontend runs on a different port (e.g., `http://localhost:4200`), requests will be allowed.

### Endpoints Overview

- **Register:** `POST /api/users/register/`
- **Login:** `POST /api/users/login/`
- **Logout:** `POST /api/users/logout/`
- **Todos CRUD:** `/api/todos/`
- **Categories:** `/api/todos/categories/`
- **Tags:** `/api/todos/tags/`
- **Comments:** `/api/todos/comments/` and `/api/todos/<todo_id>/comments/`

### Data Model Overview

#### Todos
- **What:** The core tasks you want to manage.
- **Fields:** Title, description, completed status, priority, timestamps, etc.
- **Connections:** 
  - Belongs to a user.
  - Belongs to a category.
  - Can have multiple tags.
  - Can have multiple comments.

#### Categories
- **What:** Help you group and filter your todos for better organization (e.g., "Work", "Personal").
- **Fields:** Name, description, owner (user).
- **Connections:** 
  - Each user can have many categories.
  - Each category can have many todos, but each todo belongs to one category.

#### Tags
- **What:** Flexible labels you can attach to todos (e.g., "urgent", "home").
- **Fields:** Name.
- **Connections:** 
  - Each tag can be attached to many todos, and each todo can have many tags (many-to-many).

#### Comments
- **What:** Notes or discussions attached to a todo.
- **Fields:** Text, author (user), timestamp, and the todo it belongs to.
- **Connections:** 
  - Each comment is linked to a single todo.
  - Each comment is linked to the user who wrote it.

#### How are they connected?
- **User ⟶ Category (one-to-many):** Each user can have many categories.
- **User ⟶ Todo (one-to-many):** Each user can have many todos.
- **Category ⟶ Todo (one-to-many):** Each category can have many todos, but each todo belongs to one category.
- **Tag ⟷ Todo (many-to-many):** Todos can have multiple tags, and tags can be attached to multiple todos.
- **Todo ⟶ Comment (one-to-many):** Each todo can have many comments.
- **User ⟶ Comment (one-to-many):** Each user can write many comments.

#### Example
- User "Alice" creates a category "Work".
- She adds a todo "Finish report" in the "Work" category.
- She tags it with "urgent" and "office".
- She (or a collaborator) adds a comment: "Remember to include Q1 data!"

**In summary:**
- **Todos** are your tasks.
- **Categories** group your todos.
- **Tags** label your todos.
- **Comments** are notes on your todos.
- All are connected through Django model relationships, making your app flexible and organized!

### Example: How to Authenticate and Use the API

1. **Register a user:**
   ```http
   POST /api/users/register/
   {
     "username": "yourname",
     "email": "your@email.com",
     "password": "yourpassword"
   }
   ```

2. **Login to get tokens:**
   ```http
   POST /api/users/login/
   {
     "username": "yourname",
     "password": "yourpassword"
   }
   ```
   - Response will include `access` and `refresh` tokens.

3. **Use the access token:**
   - Add this header to all requests that require authentication:
     ```
     Authorization: Bearer <access_token>
     ```

4. **Example: Get your todos**
   ```http
   GET /api/todos/
   Authorization: Bearer <access_token>
   ```

### Notes

- If you get a CORS error, make sure your frontend origin is allowed in the backend settings.
- All endpoints require authentication unless otherwise specified.
- For more details on endpoints and request/response formats, see the backend code or ask the backend team.

---
