# Development Guide

## Prerequisites
- Node.js 18+ (tested with v20)
- Python 3.11+ (tested with v3.14)
- Java 17+ (for Android builds)
- PostgreSQL 15+
- Redis 7+

## Initial Setup

### Backend
1. Create virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up env:
   - Copy `.env.example` to `.env`
   - Update DB credentials

### Mobile
1. Install dependencies:
   ```bash
   cd mobile
   npm install
   ```
2. Start Metro Bundler:
   ```bash
   npm start
   ```
3. Run on Android:
   ```bash
   npm run android
   ```

## Workflow Protocol
We follow a strict **Milestone Execution Protocol**:
1. Identify milestone in TASKS.md
2. Create implementation plan artifacts
3. Get approval
4. Execute & Verify
5. Summarize session

**Do not bypass this process.**
