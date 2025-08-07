# IraAI-backend

IraAI-backend is a Flask-based REST API that provides authentication, prompt management, and AI integration for the IraAI application. It supports JWT-based authentication, SQLAlchemy ORM, and integration with external AI services such as Mistral and Groq.

## Features

- User registration and login with JWT authentication
- Secure password hashing
- Prompt submission and response storage
- Integration with Mistral and Groq AI APIs
- CORS support for frontend integration
- Environment-based configuration using `.env` files

## Project Structure

```
backEnd-IraAI/
├── app.py
├── models.py
├── extensions.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   └── openai.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Setup & Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Srinivascvadla/IraAI-backend.git
   cd IraAI-backend
   ```

2. **Create and activate a virtual environment:**

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Create a `.env` file:**

   ```
   DATABASE_URI=sqlite:///iraai.db
   JWT_SECRET_KEY=your-very-secret-key
   JWT_EXPIRES_HOURS=2
   MISTRAL_API_KEY=your-mistral-api-key
   GROQ_API_KEY=your-groq-api-key
   ```

5. **Run the application:**
   ```sh
   flask --app app run
   ```

## API Endpoints

### Authentication

- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive JWT token

### Prompts

- `POST /iraai/prompt` — Submit a prompt (JWT required)

## Notes

- **Do not commit your `.env` file** or any secrets to version control.
- Make sure to rotate any API keys if they are accidentally exposed.

## License

This project is for learning purposes.
