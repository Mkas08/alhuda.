# Al-Huda Developer Documentation

Welcome to the Al-Huda Quran Habit Builder documentation.

## Directory Structure

- `mobile/`: React Native application (iOS & Android)
- `backend/`: FastAPI backend server
- `docs/`: Technical documentation (you are here)

## Getting Started

1. **Mobile:**
   ```bash
   cd mobile
   npm install
   npm run android
   ```

2. **Backend:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

## Key Resources
- [API Documentation](API.md)
- [Database Schema](DATABASE.md)
- [Development Guide](DEVELOPMENT.md)
