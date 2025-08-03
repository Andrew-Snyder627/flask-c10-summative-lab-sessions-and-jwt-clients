# Productivity Tracker Backend (Session Auth)

This is a secure Flask API backend that supports **user authentication via sessions**, and allows users to manage their own personal productivity data (e.g., tasks). It is designed to integrate with a provided React frontend (`client-with-sessions`) that handles login, signup, and session checking.

---

## ✨ Features

- Session-based user authentication (`/signup`, `/login`, `/logout`, `/check_session`)
- Passwords securely hashed using Bcrypt
- Full CRUD operations for user-specific tasks
- Route protection: users can only access their own tasks
- Pagination support for task listing
- Fully integrated with React frontend client

---

## 📁 Project Structure

```
/client-with-sessions
  └── /server
        ├── app.py
        ├── config.py
        ├── models.py
        ├── seed.py
        ├── migrations/
        ├── Pipfile
        ├── Pipfile.lock
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/YourUsername/your-repo-name.git
cd client-with-sessions/server
```

### 2. Install dependencies

```bash
pipenv install
pipenv shell
```

### 3. Set up the database

```bash
export FLASK_APP=app.py
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 4. Seed the database (optional)

```bash
pipenv run python seed.py
```

### 5. Run the server

```bash
flask run --port=5555
```

---

## 🧪 Testing the Frontend

1. Open a new terminal:

   ```bash
   cd client-with-sessions
   npm install
   npm start
   ```

2. Open your browser to:

   ```
   http://localhost:3000
   ```

3. Log in using:
   ```
   Username: demo
   Password: password
   ```

---

## 🔐 Authentication Endpoints

| Method | Endpoint         | Description                          |
| ------ | ---------------- | ------------------------------------ |
| POST   | `/signup`        | Register a new user & log them in    |
| POST   | `/login`         | Authenticate and create a session    |
| GET    | `/check_session` | Check if the user is still logged in |
| DELETE | `/logout`        | End the current session              |

---

## 📋 Task Resource Endpoints

> All routes require a valid session (user must be logged in)

| Method | Endpoint                   | Description                        |
| ------ | -------------------------- | ---------------------------------- |
| GET    | `/tasks?page=1&per_page=5` | Get paginated list of user’s tasks |
| POST   | `/tasks`                   | Create a new task                  |
| PATCH  | `/tasks/<id>`              | Update a task                      |
| DELETE | `/tasks/<id>`              | Delete a task                      |

### Example JSON for POST/PATCH

```json
{
  "title": "Finish lab",
  "description": "Finish endpoints and write the README"
}
```

---

## 🌱 Seed Data

Running `seed.py` will create:

- One user: `demo` / `password`
- Ten example tasks for that user

---

## ✅ Technologies Used

- Python 3.13
- Flask 2.2.2
- Flask-SQLAlchemy
- Flask-Bcrypt
- Flask-Migrate
- Flask-CORS
- Marshmallow
- Faker
- SQLite (via SQLAlchemy)

---

## 🧠 Notes

- All task endpoints are protected using `session['user_id']`
- Passwords are never exposed in responses
- Tasks are user-owned — no cross-user access is allowed
- Pagination is controlled via `?page=` and `?per_page=` query params

---

## 🗂 Example `.env` (if used)

No `.env` needed for this project, but you could replace the hardcoded `app.secret_key` with:

```bash
export SECRET_KEY="your_secret"
```

---

## 🏁 Final Notes

This backend was developed as part of a full-stack lab to practice implementing secure authentication, route protection, and user resource isolation using sessions.

Frontend repo:  
📁 `client-with-sessions/`
