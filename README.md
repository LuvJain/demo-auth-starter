# Auth System Starter

Minimal FastAPI application ready for JWT authentication implementation.

## Structure

```
app/
├── main.py          # Basic FastAPI app with public endpoint
├── api/             # Empty - ready for auth.py (login/signup)
└── models/
    └── user.py      # Basic User model (no password field yet)
```

## What's Missing (To Be Implemented)

- `python-jose[cryptography]` - JWT token generation
- `passlib[bcrypt]` - Password hashing
- `app/auth/jwt.py` - JWT utilities
- `app/auth/middleware.py` - Auth middleware/dependency
- `app/api/auth.py` - Login and signup endpoints
- Password field in User model

## Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit: http://localhost:8000
